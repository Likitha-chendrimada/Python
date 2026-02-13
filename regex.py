import re
def numberMatcher(s):
    pat=r'\d+'   # matches one or more digits
    match=re.findall(pat, s)   # finds all numbers
    if match:
        for i in match:
            print(i, end=" ")
    else:
        print(-1, end="")
