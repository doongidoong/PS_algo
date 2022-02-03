import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
def DFS(v):     
  for i in range(1, n + 1):
    if ch[i] == 0 and g[v][i] == 1:
        ch[i] = 1
        DFS(i)


n,m = map(int,input().split())
g = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(m):
    a,b =map(int,input().split())
    g[a][b] =1
    g[b][a] =1 

cnt=0
ch=[0 for _ in range(n+1)]
    
for i in range(1,n+1):
    if ch[i]==0:
        ch[i]=1
        DFS(i)
        cnt+=1

print(cnt)