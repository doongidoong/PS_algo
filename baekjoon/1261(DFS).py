from cmath import inf
from collections import deque
import sys

sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n,m=map(int, input().split())

a = [list(map(int,input())) for _ in range(m)]
q = deque()


dx=[0,0,-1,1]
dy=[-1,1,0,0]
q.append((0,0))
dis = [[-1]*(n) for _ in range(m)]
dis[0][0] = 0

next =deque()
while q:
    x,y= q.popleft()
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<=m-1 and 0<=yy<=n-1 and dis[xx][yy] == -1:
            if a[xx][yy] == 0:
                dis[xx][yy] = dis[x][y]
                q.appendleft((xx,yy))
            if a[xx][yy] == 1:
                dis[xx][yy] = dis[x][y]+1
                q.append((xx,yy))
   
print(dis[m-1][n-1])