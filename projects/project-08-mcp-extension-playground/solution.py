"""Project 08: MCP Extension Playground — compact reference solution."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from mcp_course.extensions import extension_supported,extension_result
def main():
    caps={"extensions":["schoolofai/demo"]}; print(extension_supported(caps,"schoolofai/demo")); print(extension_result("schoolofai/demo",{"ok":True}))

if __name__=="__main__":
    main()
