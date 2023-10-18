
def swap(L,d,move):
    if d==0:
        for i in range(move):
            a= L.pop(0)
            L.append(a)

    else:
        for i in range(move):
            a = L.pop()
            L.insert(0,a)
    return L

import sys
#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")

n = int(input())
L = [list(map(int, input().split())) for i in range(n)]

m = int(input())
for i in range(m):
    a, b,c = map(int, input().split())
    L[a-1] = swap(L[a-1],b,c)


tot= 0
s=0
e=n
for i in range(n):
    for j in range(s,e):
        tot +=L[i][j]
    if i< n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1

print(tot)
