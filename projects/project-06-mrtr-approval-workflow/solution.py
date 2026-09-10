"""Project 06: MRTR Approval Workflow — compact reference solution."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from mcp_course.mrtr import input_required,attach_input_responses
def main():
    req=input_required("r1",[{"id":"approve","prompt":"Approve refund?"}])
    print(req); print(attach_input_responses({"amount":100},{"approve":True}))

if __name__=="__main__":
    main()
