"""Project 14: MCP Knowledge & RAG Service — compact reference solution."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from mcp_course.resources import Resource,ResourceCatalog
def main():
    r=ResourceCatalog(); r.add(Resource("kb://hr/leave","Leave","20 days",{"employee","manager"})); r.add(Resource("kb://finance/expense","Expense","director approval",{"manager"}))
    print(r.list(("employee",)))

if __name__=="__main__":
    main()
