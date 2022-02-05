import sys
from collections import deque
#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

n = int(input())


board = [list(map(int, input())) for _ in range(n)]
res = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            Q = deque()
            cnt=0
            Q.append((i,j))
            board[i][j]=0
            while Q:
                p = Q.popleft()
                cnt+=1
                for s in range(4):
                    x= p[0] +dx[s]
                    y= p[1] +dy[s]
                    if 0<=x<=n-1 and 0<=y<=n-1 and board[x][y]==1:
                        Q.append((x,y))
                        board[x][y]=0
            res.append(cnt)
res.sort()
print(len(res))
for i in res:
    print(i)