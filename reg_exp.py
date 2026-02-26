import re
def validate(str):
    pat = r'^[a-z]+[!@#$%]+[0-9]+$'
    return bool(re.fullmatch(pat,str))
