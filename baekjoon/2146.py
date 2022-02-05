import sys
from collections import deque
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n = int(input())


board = [list(map(int, input().split())) for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
Q = deque() 
ch = [[0 for _ in range(n)] for _ in range(n)]
res= n*n
for i in range(n):
    for j in range(n):
        dis = [[ 0 for _ in range(n)] for _ in range(n)]
        if ch[i][j]==0 and board[i][j]==1:
            Q.append((i,j))
            Q2= deque()
            ch[i][j] =1
            while Q:
                p = Q.popleft()
                for i in range(4):
                    x = p[0] + dx[i]
                    y = p[1] + dy[i]
                    if 0<=x<=n-1 and 0<=y<=n-1 :
                        if ch[x][y] == 0 and board[x][y]==1:
                            ch[x][y] = 1
                            Q.append((x,y))
                        if board[x][y]==0:
                            Q2.append((x,y))
                            dis[x][y] = 1 
            while Q2:
                p = Q2.popleft()
                for i in range(4):
                    x = p[0] + dx[i]
                    y = p[1] + dy[i]
                    if 0<=x<=n-1 and 0<=y<=n-1 :
                        if dis[x][y] == 0 and board[x][y]==0:
                            dis[x][y] = dis[p[0]][p[1]]+1
                            Q2.append((x,y))
                        if ch[x][y] == 0 and board[x][y]==1:
                            res = dis[p[0]][p[1]]
                            break
                if res <= dis[p[0]][p[1]]:
                    Q2.clear()
print(res)