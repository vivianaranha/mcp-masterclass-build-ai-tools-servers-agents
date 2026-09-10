"""Project 02: Local MCP Tool Server — compact reference solution."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from mcp_course.tools import Tool,ToolRegistry
def main():
    reg=ToolRegistry(); reg.register(Tool("add","Add numbers",lambda a,b:a+b,{"a","b"},False,{"math.use"}))
    print(reg.list()); print(reg.call("add",{"a":2,"b":3},{"math.use"}))

if __name__=="__main__":
    main()
