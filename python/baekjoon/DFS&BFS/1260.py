import sys
from collections import deque
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

def DFS(v):
  ch[v] = 1        
  print(v, end = " ")
  for i in range(1, n + 1):
    if ch[i] == 0 and g[v][i] == 1:
      DFS(i)

check=0
n,m,v = map(int,input().split())
g = [[0 for _ in range(n+1)] for _ in range(n+1)]
ch=[0 for _ in range(n+1)]
res = [0]*n
for i in range(m):
    a,b =map(int,input().split())
    g[a][b] =1
    g[b][a] =1 


ch[v]=1
res[0]=v
DFS(v)

print()
ch=[0 for _ in range(n+1)]
ch[v]=1
Q =deque()
Q.append(v)

while Q:
    p = Q.popleft()
    print(p,end=' ')
    for i in range(1,n+1):
        if ch[i]==0 and g[p][i]==1:
            ch[i]=1
            Q.append(i)

