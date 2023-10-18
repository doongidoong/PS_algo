import sys
from collections import deque
#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")
n = int(input())  

board = [list(map(int, input().split())) for _ in range(n)]
Q = deque()
dx =[1,-1,0,0,1,1,-1,-1]
dy =[0,0,1,-1,1,-1,1,-1]



cnt=0
for p1 in range(n):
    for p2 in range(n):
        if board[p1][p2]==1:
            Q.append((p1,p2))
            while Q:
                p = Q.popleft()
                board[p[0]][p[1]]=0 
                for i in range(8):
                    a = p[0]+dx[i]
                    b = p[1]+dy[i]
                    if 0<=a<=n-1 and 0<=b<=n-1 and board[a][b]==1:
                        Q.append((a,b))
            cnt+=1
            

print(cnt)

