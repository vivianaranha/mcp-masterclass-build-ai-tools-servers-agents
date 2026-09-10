def input_required(request_id,questions): return {"resultType":"input_required","requestId":request_id,"requests":questions}
def attach_input_responses(original_params,responses):
    value=dict(original_params); value["inputResponses"]=responses; return value
