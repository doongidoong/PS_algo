
from cmath import inf
import sys
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\baekjoon\\input.txt","rt")

n= int(input())

L = list(map(int,input().split()))

dy=[inf for _ in range(n)]

dy[0]=0
for i in range(n):
    temp = dy[i]
    ran = min(L[i]+1,n-i)
    for j in range(1,ran):
        dy[i+j] = min(dy[i+j],temp+1)

if dy[-1]==inf:
    print(-1)
else :
    print(dy[-1])
