from dataclasses import dataclass
@dataclass
class Token:
    issuer:str; audience:str; subject:str; scopes:set[str]
def validate_token(token,expected_issuer,expected_audience,required_scopes):
    if token.issuer!=expected_issuer: raise PermissionError("issuer mismatch")
    if token.audience!=expected_audience: raise PermissionError("audience mismatch")
    if not set(required_scopes).issubset(token.scopes): raise PermissionError("insufficient scope")
    return True
