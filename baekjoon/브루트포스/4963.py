import sys
from collections import deque
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

while(1):
    w,h = map(int, input().split())
    if w ==0 and h ==0 :
        break
    board = [list(map(int, input().split())) for _ in range(h)]
    res = []
    dx = [0,0,1,-1,1,1,-1,-1]
    dy = [1,-1,0,0,1,-1,1,-1]
    cnt=0
    for i in range(h):
        for j in range(w):
            if board[i][j]==1:
                Q = deque()
                Q.append((i,j))
                board[i][j]=0
                while Q:
                    p = Q.popleft()
                    for s in range(8):
                        x= p[0] +dx[s]
                        y= p[1] +dy[s]
                        if 0<=x<=h-1 and 0<=y<=w-1 and board[x][y]==1:
                            Q.append((x,y))
                            board[x][y]=0
                cnt+=1
    print(cnt)