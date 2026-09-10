class LocalMCPServer:
    def __init__(self,tools,resources,prompts): self.tools=tools; self.resources=resources; self.prompts=prompts
    def handle(self,request,scopes=(),roles=()):
        m=request.method
        if m=="tools/list": return {"tools":self.tools.list(),"ttlMs":60000,"cacheScope":"public"}
        if m=="tools/call": return self.tools.call(request.name,request.params.get("arguments",{}),scopes)
        if m=="resources/list": return {"resources":self.resources.list(roles),"ttlMs":60000,"cacheScope":"private"}
        if m=="resources/read": return self.resources.read(request.params["uri"],roles)
        if m=="prompts/list": return {"prompts":self.prompts.list(),"ttlMs":60000,"cacheScope":"public"}
        if m=="prompts/get": return {"prompt":self.prompts.render(request.name,request.params.get("arguments",{}))}
        raise ValueError("unsupported method")
