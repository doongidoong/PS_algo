import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
sys.setrecursionlimit(10**6)
n = int(input())
g = [[] for _ in range(n+1)]
ch =[0 for _ in range(n+1)]

for i in range(n-1):
    a,b,c = map(int, input().split())
    g[a].append((b,c))
    g[b].append((a,c))

res=0
nod=-1
def DFS(v,r):
    global res,nod
    if res<r:
        res=r
        nod=v  
    for now in g[v]:
        point = now[0]
        dis  = now[1]
        if ch[point] == 0:
            ch[point]=1
            DFS(point,r+dis) 
            ch[point]=0
ch[1]=1
DFS(1,0)
ch[1]=0
ch[nod]=1
DFS(nod,0)
print(res)