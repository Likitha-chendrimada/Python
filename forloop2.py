#for a given string s, print its characters at even indices(index starts at 0). 

def stringJumper(s):
    for i in range(0,len(s),2):
        # from 0 to length of str and skip 2
        print(s[i],end="")
