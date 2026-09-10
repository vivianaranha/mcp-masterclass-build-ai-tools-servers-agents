from dataclasses import dataclass,field
from uuid import uuid4
@dataclass
class Task:
    task_id:str; status:str="working"; progress:int=0; result:object|None=None; error:str|None=None; history:list=field(default_factory=list)
class TaskStore:
    def __init__(self): self.tasks={}
    def create(self):
        t=Task(str(uuid4())); self.tasks[t.task_id]=t; return t
    def get(self,task_id): return self.tasks[task_id]
    def update(self,task_id,progress=None,result=None,error=None):
        t=self.tasks[task_id]
        if progress is not None: t.progress=progress
        if error is not None: t.error=error; t.status="failed"
        elif result is not None: t.result=result; t.progress=100; t.status="completed"
        t.history.append((t.status,t.progress)); return t
    def cancel(self,task_id):
        t=self.tasks[task_id]; t.status="cancelled"; t.history.append((t.status,t.progress)); return t
