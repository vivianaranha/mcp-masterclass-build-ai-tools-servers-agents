"""Project 12: MCP Gateway & Policy Router — compact reference solution."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from mcp_course.gateway import PolicyGateway
def main():
    g=PolicyGateway({("tools/call","get_ticket"):"support-server"},{("tools/call","get_ticket"):{"employee"}},2)
    print(g.route({"Mcp-Method":"tools/call","Mcp-Name":"get_ticket"},"u1",("employee",)))

if __name__=="__main__":
    main()
