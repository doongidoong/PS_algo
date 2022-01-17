
import sys
from collections import deque

sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")

n = int(input())
L=[]
for i in range(n):
    L.append(list(map(int, input().split())))


y = n//2
x = n//2
dq = deque()
dq.append((x,y))
ch =[]
for i in range(n):
    ch.append([0]*n)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

sum = L[x][y]
ch[x][y] =1 
Lev=0
while( 1) :
    if Lev==n//2:
        break
    size = len(dq)
    for j in range(size):
        p=dq.popleft()
        for i in range(4):
            a, b = p[0]+dx[i] , p[1]+dy[i]
            if ch[a][b] ==0:
                dq.append((a, b))
                ch[a][b] =1
                sum+=L[a][b]
    Lev+=1

print(sum)

