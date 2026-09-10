import sys
from pathlib import Path
import unittest
sys.path.append(str(Path(__file__).resolve().parents[1]/"src"))
from mcp_course.messages import MCPRequest
from mcp_course.tools import Tool,ToolRegistry
from mcp_course.resources import Resource,ResourceCatalog
from mcp_course.prompts import PromptCatalog
from mcp_course.auth import Token,validate_token
from mcp_course.tasks import TaskStore
from mcp_course.mrtr import input_required,attach_input_responses
from mcp_course.gateway import PolicyGateway
from mcp_course.extensions import extension_supported,extension_result
from mcp_course.cache import TTLCache
from mcp_course.server import LocalMCPServer
from mcp_course.client import LocalClient

class MCPTests(unittest.TestCase):
    def test_headers(self):
        h=MCPRequest(1,"tools/call",{},"x").headers(); self.assertEqual(h["Mcp-Method"],"tools/call"); self.assertEqual(h["Mcp-Name"],"x")
    def test_tool_scope(self):
        r=ToolRegistry(); r.register(Tool("x","x",lambda a:a,{"a"},False,{"read"})); self.assertEqual(r.call("x",{"a":2},{"read"}),2)
        with self.assertRaises(PermissionError): r.call("x",{"a":2},set())
    def test_resource_roles(self):
        c=ResourceCatalog(); c.add(Resource("u","n","t",{"manager"})); self.assertEqual(c.list(("employee",)),[])
        with self.assertRaises(PermissionError): c.read("u",("employee",))
    def test_prompt(self):
        p=PromptCatalog(); p.add("g","Hi {name}",{"name"}); self.assertEqual(p.render("g",{"name":"A"}),"Hi A")
    def test_auth(self):
        t=Token("iss","aud","u",{"read"}); self.assertTrue(validate_token(t,"iss","aud",{"read"}))
        with self.assertRaises(PermissionError): validate_token(t,"bad","aud",{"read"})
    def test_task(self):
        s=TaskStore(); t=s.create(); s.update(t.task_id,progress=20); s.update(t.task_id,result="ok"); self.assertEqual(s.get(t.task_id).status,"completed")
    def test_cancel(self):
        s=TaskStore(); t=s.create(); self.assertEqual(s.cancel(t.task_id).status,"cancelled")
    def test_mrtr(self):
        self.assertEqual(input_required("1",[])["resultType"],"input_required"); self.assertIn("inputResponses",attach_input_responses({}, {"a":1}))
    def test_gateway(self):
        g=PolicyGateway({("tools/call","x"):"s"},{("tools/call","x"):{"employee"}},1); self.assertEqual(g.route({"Mcp-Method":"tools/call","Mcp-Name":"x"},"u",("employee",)),"s")
        with self.assertRaises(RuntimeError): g.route({"Mcp-Method":"tools/call","Mcp-Name":"x"},"u",("employee",))
    def test_extension(self):
        self.assertTrue(extension_supported({"extensions":["a/b"]},"a/b")); self.assertEqual(extension_result("a/b",{"x":1})["extension"],"a/b")
    def test_cache(self):
        c=TTLCache(); c.put("x",1,10000); self.assertEqual(c.get("x"),1)
    def test_client_cache(self):
        r=ToolRegistry(); r.register(Tool("x","x",lambda:1)); s=LocalMCPServer(r,ResourceCatalog(),PromptCatalog()); c=LocalClient(s); self.assertEqual(c.list_tools(),c.list_tools())
if __name__=="__main__": unittest.main()
