"""Project 07: MCP Tasks Engine — compact reference solution."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from mcp_course.tasks import TaskStore
def main():
    s=TaskStore(); t=s.create(); s.update(t.task_id,progress=50); s.update(t.task_id,result={"done":True}); print(s.get(t.task_id))

if __name__=="__main__":
    main()
