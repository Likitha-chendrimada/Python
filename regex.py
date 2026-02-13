##Write a Python function numberMatcher(str) that uses Regular Expressions to extract and print all numbers present in the given string str.
##If numbers are found, print them separated by space.
##If no numbers are found, print -1.




import re
def numberMatcher(s):
    pat=r'\d+'   # matches one or more digits
    match=re.findall(pat, s)   # finds all numbers
    if match:
        for i in match:
            print(i, end=" ")
    else:
        print(-1, end="")
