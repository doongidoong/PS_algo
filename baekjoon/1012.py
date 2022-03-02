import sys
from collections import deque
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

dx =[0,0,1,-1]
dy =[1,-1,0,0]
def BFS(Q):
    while Q:
        a,b=Q.popleft()
        for i in range(4):
            x= a+dx[i]
            y =b+dy[i]
            if 0<=x<=n-1 and 0<=y<=m-1 and g[x][y]==1:
                g[x][y]=0
                Q.append((x,y))

            


t = int(input())
for i in range(t):
    m,n,k = map(int,input().split())
    g=[[0 for _ in range(m) ] for _ in range(n)]

    for i in range(k):
        a,b = map(int,input().split())
        g[b][a]=1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if g[i][j]==1:
                Q = deque()
                cnt+=1
                g[i][j]=0
                Q.append((i,j))
                BFS(Q)
    print(cnt)