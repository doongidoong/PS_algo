import sys
def reverse(L):
    return L[::-1]


#sys.stdin = open("input.txt","rt")
L = list(range(1,21))
for i in range(10):
    a,b = map(int,input().split())
    L[a-1:b] = reverse(L[a-1:b])
    
for i in L:
    print(i,end =" ")


    