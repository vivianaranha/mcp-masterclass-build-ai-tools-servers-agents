from dataclasses import dataclass,field
from typing import Callable,Any
@dataclass
class Tool:
    name:str; description:str; fn:Callable[...,Any]
    required:set[str]=field(default_factory=set); write:bool=False; required_scopes:set[str]=field(default_factory=set)
class ToolRegistry:
    def __init__(self): self.tools={}
    def register(self,tool): self.tools[tool.name]=tool
    def list(self): return [{"name":t.name,"description":t.description,"write":t.write} for t in self.tools.values()]
    def call(self,name,arguments,scopes=()):
        tool=self.tools[name]; missing=tool.required-set(arguments)
        if missing: raise ValueError(f"missing arguments: {sorted(missing)}")
        if not tool.required_scopes.issubset(set(scopes)): raise PermissionError("insufficient scope")
        return tool.fn(**arguments)
