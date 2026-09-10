from dataclasses import dataclass
@dataclass
class Resource:
    uri:str; name:str; text:str; roles:set[str]; mime_type:str="text/plain"; ttl_ms:int=60000
class ResourceCatalog:
    def __init__(self): self.items={}
    def add(self,r): self.items[r.uri]=r
    def list(self,roles=()):
        rs=set(roles)
        return [{"uri":r.uri,"name":r.name,"mimeType":r.mime_type,"ttlMs":r.ttl_ms} for r in self.items.values() if not r.roles or r.roles.intersection(rs)]
    def read(self,uri,roles=()):
        r=self.items[uri]; rs=set(roles)
        if r.roles and not r.roles.intersection(rs): raise PermissionError("resource access denied")
        return {"uri":r.uri,"mimeType":r.mime_type,"text":r.text,"ttlMs":r.ttl_ms}
