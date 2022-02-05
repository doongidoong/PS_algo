import sys
from collections import deque
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n = map(int, input())


board = [list(map(int, input().split())) for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
Q = deque() 
dis = [[0 for _ in range(n)] for _ in range(n)]
res =n*n
for i in range(n):
    for j in range(n):
        if 
dis[0][0] =1 
while Q :
    p = Q.popleft()
    for i in range(4):
        x = p[0] + dx[i]
        y = p[1] + dy[i]
        if 0<=x<=h-1 and 0<=y<=w-1 and dis[x][y] == 0 and board[x][y]==1:
            dis[x][y] = dis[p[0]][p[1]]+1
            Q.append((x,y))
print(dis[h-1][w-1])