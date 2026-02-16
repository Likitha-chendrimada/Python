"""Return True for the following cases:
Either a or b (not both) is non-negative and the flag is false.
Both a and b are negative and the flag is true.
Otherwise, return False."""


class Solution:
    def checkStatus(self,a,b,flag):
        if flag:
            return a<0 and b<0
        else:
            return (a>=0)^(b>=0)
