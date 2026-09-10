"""Project 05: MCP Client & Discovery Cache — compact reference solution."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from mcp_course.tools import Tool,ToolRegistry
from mcp_course.resources import ResourceCatalog
from mcp_course.prompts import PromptCatalog
from mcp_course.server import LocalMCPServer
from mcp_course.client import LocalClient
def main():
    reg=ToolRegistry(); reg.register(Tool("ping","Ping",lambda:"pong"))
    c=LocalClient(LocalMCPServer(reg,ResourceCatalog(),PromptCatalog()))
    print(c.list_tools()); print(c.list_tools())

if __name__=="__main__":
    main()
