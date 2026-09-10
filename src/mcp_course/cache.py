from time import time
class TTLCache:
    def __init__(self): self.data={}
    def put(self,key,value,ttl_ms): self.data[key]=(value,time()+ttl_ms/1000)
    def get(self,key):
        value=self.data.get(key)
        if not value: return None
        payload,expires=value
        if time()>expires: self.data.pop(key,None); return None
        return payload
