
#Given an integer n, which can be positive, negative, or zero:
#If n < 0, print numbers from n to 0 by increasing 1 each time.
#If n > 0, print numbers from n-1 to 0 by decreasing 1 each time.
#If n = 0, print "already Zero".
def pos(n):
    for i in range(n-1,-1,-1):
        print(i,end=" ")
def neg(n):
    for i in range(n,1):
        print(i,end=" ")
def check(n):
    if n==0:
        print("already Zero")
    elif n>0:
        pos(n)
    else:
        neg(n)
