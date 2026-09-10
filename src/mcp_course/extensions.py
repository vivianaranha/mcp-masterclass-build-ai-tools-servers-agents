def extension_supported(capabilities,extension_name): return extension_name in set(capabilities.get("extensions",[]))
def extension_result(namespace,payload):
    if "/" not in namespace: raise ValueError("namespaced extension required")
    return {"extension":namespace,"payload":payload}
