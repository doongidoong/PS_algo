import sys
from collections import deque
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
w,h = map(int, input().split())


board = [list(map(int, input().split())) for _ in range(h)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
Q = deque()       
            
for i in range(h):
    for j in range(w):
        if board[i][j]==1:
            Q.append((i,j))
            board[i][j]=-1
cnt=0
temp = Q
while temp:
    Q = temp
    temp=deque()
    while Q:
        p = Q.popleft()
        for s in range(4):
            x= p[0] +dx[s]
            y= p[1] +dy[s]
            if 0<=x<=h-1 and 0<=y<=w-1 and board[x][y]==0:
                    temp.append((x,y))
                    board[x][y]=-1
    cnt+=1
for i in range(h):
    for j in range(w):
        if board[i][j]==0:
            print(-1)
            sys.exit(0)
print(cnt-1)