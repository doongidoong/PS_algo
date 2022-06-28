import sys
from collections import deque
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")

n = int(input())
r1, c1, r2, c2 = map(int,input().split())

Q = deque()
visited = [[0]*(n) for _ in range(n)]
Q.append((r1,c1))
dx=[-2,-2,0,0,2,2]
dy=[-1,1,-2,2,-1,+1]
visited[r1][c1]=1
while Q:
    p = Q.popleft()
    x,y = p[0], p[1]
    if x== r2 and y == c2:
        print(visited[x][y]-1)
        break
    for i in range(6):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0<=xx<=n-1 and 0<=yy<=n-1 and visited[xx][yy]==0 :
            Q.append((xx,yy))
            visited[xx][yy]=visited[x][y]+1
else:
    print(-1)