import sys
from collections import deque

sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")

dx =[1,-1,0,0]

dy =[0,0,1,-1]

board = [list(map(int, input().split())) for _ in range(7)]
dis = [[0]*7 for _ in range(7)]
Q =deque()
Q.append((0,0))
board[0][0]=1
while Q:
    tmp = Q.popleft()
    for i in range(4):
        x = tmp[0]+dx[i]
        y = tmp[1]+dy[i]
        if 0<=x<= 6 and 0<=y<=6 and board[x][y] ==0:
            board[x][y] =1
            dis[x][y] = dis[tmp[0]][tmp[1]] +1
            Q.append((x,y))
if dis[6][6] ==0:
    print(-1)
else:
    print(dis[6][6])
"""
# 내 풀이
a=[[1]*9]
for i in range(7):
    a.append([1]+list(map(int, input().split()))+[1])

a.append([1]*9)

d =list([0]*9 for _ in range(9))

Q = deque()
dx =[1,-1,0,0]

dy =[0,0,1,-1]
Q.append((1,1))
check=0
while(Q):
    p = Q.popleft()
    if p[0]  == 7 and p[1] == 7:
        check=1
        break
    for i in range(4): 
        x = p[0]+dx[i]
        y = p[1]+dy[i]
        if a[x][y] ==0 and d[x][y]==0:
            Q.append((x,y))
            d[x][y] = d[p[0]][p[1]] +1
if check==0 :
    print(-1)
else:
    print(d[7][7])
"""