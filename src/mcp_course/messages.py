from dataclasses import dataclass
@dataclass
class MCPRequest:
    request_id: str|int
    method: str
    params: dict
    name: str|None=None
    def headers(self):
        h={"Content-Type":"application/json","Mcp-Method":self.method}
        if self.name: h["Mcp-Name"]=self.name
        return h
    def body(self): return {"jsonrpc":"2.0","id":self.request_id,"method":self.method,"params":self.params}
def result(request_id,value): return {"jsonrpc":"2.0","id":request_id,"result":value}
def error(request_id,code,message): return {"jsonrpc":"2.0","id":request_id,"error":{"code":code,"message":message}}
