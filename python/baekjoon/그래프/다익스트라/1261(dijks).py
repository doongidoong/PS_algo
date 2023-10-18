from heapq import heappush, heappop
import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

n,m = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

visit = [[0] * m for i in range(n)]

a = [list(map(int,input())) for _ in range(n)]

q =[]
heappush(q,(0,0,0))
visit[0][0]=1
while q:
    c,x,y = heappop(q)
    if x == n-1 and y==m-1:
        print(c)
        break
    for i in range(4):
        xx= x+dx[i]
        yy= y+dy[i]
        if 0<= xx<=n-1 and 0<=yy<=m-1 and visit[xx][yy]==0:
            visit[xx][yy]= 1
            if a[xx][yy] == 0:
                heappush(q,(c,xx,yy))
            if a[xx][yy] == 1:
                heappush(q,(c+1,xx,yy))
