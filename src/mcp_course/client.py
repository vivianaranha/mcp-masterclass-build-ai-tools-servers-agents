from .cache import TTLCache
class LocalClient:
    def __init__(self,server): self.server=server; self.cache=TTLCache()
    def list_tools(self,ttl_ms=60000):
        cached=self.cache.get("tools")
        if cached is not None: return cached
        value=self.server.tools.list(); self.cache.put("tools",value,ttl_ms); return value
