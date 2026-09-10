"""Project 01: MCP Message Inspector — compact reference solution."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from mcp_course.messages import MCPRequest
def main():
    r=MCPRequest(1,"tools/call",{"arguments":{"ticket_id":"T1"}},"get_ticket")
    print({"headers":r.headers(),"body":r.body()})

if __name__=="__main__":
    main()
