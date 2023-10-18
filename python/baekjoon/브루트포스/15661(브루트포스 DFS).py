#카잉달력
from cmath import inf
import sys
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")

n = int(input())
a =[  list(map(int, input().split())) for _ in range(n)]
check = [0]*n

answer = inf

def DFS(L,s,end):
    global answer
    if L==end:
        temp=0
        for i in range(n):
            if i in res:
                for j in res:
                    temp+=a[i][j]
            else:
                for j in [k for k in range(n) if k not in res]:
                    temp-=a[i][j]
        answer = min(answer,abs(temp))
        return
    for i in range(s,n):
        if check[i]==0:
            res[L]=i
            check[i]=1
            DFS(L+1,i,end)
            check[i]=0 
check[0]= 1
for i in range(1,n-1):
    res = [0]*(i)
    DFS(1,0,i)

print(answer)