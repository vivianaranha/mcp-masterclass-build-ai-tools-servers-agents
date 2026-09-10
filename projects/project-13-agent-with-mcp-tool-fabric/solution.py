"""Project 13: Agent with MCP Tool Fabric — compact reference solution."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from mcp_course.tools import Tool,ToolRegistry
def main():
    r=ToolRegistry(); r.register(Tool("search","Search",lambda q:{"q":q}, {"q"},False,{"knowledge.read"})); r.register(Tool("refund","Refund",lambda amount:{"amount":amount}, {"amount"},True,{"refunds.write"}))
    print(r.call("search",{"q":"leave"},{"knowledge.read"}))
    try: r.call("refund",{"amount":100},{"knowledge.read"})
    except PermissionError as e: print({"blocked":str(e)})

if __name__=="__main__":
    main()
