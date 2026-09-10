class PolicyGateway:
    def __init__(self,routes,role_permissions,rate_limit=100):
        self.routes=routes; self.role_permissions=role_permissions; self.rate_limit=rate_limit; self.counts={}
    def route(self,headers,identity,roles):
        method=headers.get("Mcp-Method"); name=headers.get("Mcp-Name"); key=(identity,method,name)
        self.counts[key]=self.counts.get(key,0)+1
        if self.counts[key]>self.rate_limit: raise RuntimeError("rate limit exceeded")
        allowed=self.role_permissions.get((method,name),set())
        if allowed and not allowed.intersection(set(roles)): raise PermissionError("gateway policy denied")
        return self.routes[(method,name)]
