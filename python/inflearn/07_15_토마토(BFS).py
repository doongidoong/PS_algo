import sys
from collections import deque
#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
n, m=map(int, input().split())
board=[list(map(int, input().split())) for _ in range(m)]
Q=deque()
dis=[[0]*n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if board[i][j]==1:
            Q.append((i, j))
while Q:
    x, y=Q.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<m and 0<=ny<n and board[nx][ny]==0:
            board[nx][ny]=1 # 익은 것들은 1로 바꿈
            dis[nx][ny]=dis[x][y]+1 # 익은 토마토의 값에 +1의 값은 새로운 토마토에 넣음
            Q.append((nx, ny))
flag=1
for i in range(m):
    for j in range(n):
        if board[i][j]==0:
            flag=0
result=0
if flag==1:
    for i in range(m):
        for j in range(n):
            if dis[i][j]>result:
                result=dis[i][j]
    print(result)
else:
    print(-1)


"""
내풀이

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
n ,m = map(int, input().split())
board = [list(map(int, input().split()))for _ in range(m)]
Q =deque()
cnt=0
check=1
first=1
while check==1:
    check = 0
    for i in range(m):
        for j in range(n):
            if first ==1 and board[i][j]==0:
                first+=1
            if board[i][j]==1:
                Q.append((i,j))
                board[i][j] = -1
                check=1
    if first==1:
        break
    if check==0:
        break
    while Q:
        p= Q.popleft()
        for s in range(4):
            a = p[0]+dx[s]
            b = p[1]+dy[s]
            if 0<=a<=m-1 and 0<=b<=n-1:
                if board[a][b] == 0 :
                    board[a][b] = 1
    cnt+=1
if first ==1 :
    print(0)
    sys.exit(0)
for i in range(m):
    for j in range(n):
        if board[i][j]==0:
            print(-1)
            sys.exit(0)
print(cnt-1)

"""