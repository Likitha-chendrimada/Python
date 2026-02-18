"""You will be provided an integer named as operator. 
If operator equals to 1 add a and b, then print the result as a string.
If operator equals to 2 subtract b from a, then print the result as a string.
If operator equals to 3 multiply a and b, then print the result as a string.
If operator equals to any another number, print "Invalid Input"(without quotes)."""

def utility(a, b, opr):
    if opr==1:
        print(str(a+b),end="")
    elif opr==2:
        print(str(a-b),end="")
    elif opr==3:
        print(str(a*b),end="")
    else:
        print("Invalid Input",end="")
