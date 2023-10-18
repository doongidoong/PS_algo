import sys
from collections import deque
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
h,w = map(int, input().split())


board = [list(map(int, input())) for _ in range(h)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
Q = deque() 
dis = [[0 for _ in range(w)] for _ in range(h)]

Q.append((0,0))
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