from cmath import inf
import sys
from collections import defaultdict
sys.setrecursionlimit(10**9)
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")
n= int(input())
a = list(sys.stdin.readline().split())
s=''.join(a)
check = [0]*(n+1)

ans = inf
def DFS(L,t):
    global ans
    if t[:len(t)]<s[:len(t)]:
        return
    if L==n:
        if ans>int(t) and t>s:
            ans=int(t)
        return
    for i in range(1,n+1):
        if check[i]==0:
            check[i]=1
            DFS(L+1,t+str(i))
            check[i]=0
DFS(0,'')
if ans == inf:
    print(-1)
    
else:
    print(ans)