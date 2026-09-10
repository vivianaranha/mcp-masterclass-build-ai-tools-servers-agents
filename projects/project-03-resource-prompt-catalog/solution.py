"""Project 03: Resource & Prompt Catalog — compact reference solution."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from mcp_course.resources import Resource,ResourceCatalog
from mcp_course.prompts import PromptCatalog
def main():
    r=ResourceCatalog(); r.add(Resource("kb://leave","Leave","20 days",{"employee"}))
    p=PromptCatalog(); p.add("summarize","Summarize {topic}",{"topic"})
    print(r.list(("employee",))); print(p.render("summarize",{"topic":"leave"}))

if __name__=="__main__":
    main()
