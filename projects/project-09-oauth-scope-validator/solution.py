"""Project 09: OAuth & Scope Validator — compact reference solution."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from mcp_course.auth import Token,validate_token
def main():
    t=Token("https://idp.example","mcp://support","u1",{"tickets.read"}); print(validate_token(t,"https://idp.example","mcp://support",{"tickets.read"}))

if __name__=="__main__":
    main()
