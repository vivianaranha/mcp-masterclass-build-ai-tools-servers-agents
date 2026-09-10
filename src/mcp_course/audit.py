def audit_event(identity,method,name,outcome,details=None): return {"identity":identity,"method":method,"name":name,"outcome":outcome,"details":details or {}}
