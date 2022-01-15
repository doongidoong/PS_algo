import sys


#sys.stdin = open("input.txt","rt")

N = int(input())

for i in range(N):
    a = input()
    a = a.lower()
    size =len(a)
    for j in range(size//2):
        if a[j]!=a[size-j-1]:
            print("#%d NO"%(i+1))
            break
    else:
        print("#%d YES"%(i+1))
"""   
for i in range(N):
    a = input()
    a = a.lower()
    if a== a[::-1]:
        print("#%d YES"%(i+1))
    else:
        print("#%d NO"%(i+1))
"""
