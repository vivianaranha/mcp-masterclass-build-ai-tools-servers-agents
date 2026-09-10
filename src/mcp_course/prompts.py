class PromptCatalog:
    def __init__(self): self.prompts={}
    def add(self,name,template,required=()): self.prompts[name]={"template":template,"required":set(required)}
    def list(self): return [{"name":k,"arguments":sorted(v["required"])} for k,v in self.prompts.items()]
    def render(self,name,args):
        p=self.prompts[name]; missing=p["required"]-set(args)
        if missing: raise ValueError(f"missing prompt args: {sorted(missing)}")
        return p["template"].format(**args)
