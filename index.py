 #Given a tuple arr with distinct elements and an integer x, find the index position of x. Assume to have x in the tuple always. Print the index (0-based).

arr=tuple(map(int, input().split()))
x=int(input())
print(arr.index(x))
