import sys
from collections import deque
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
m,n=map(int , input().split())

board = [list(map(int,input().split())) for _ in range(m)]
ch =[ [0 for _ in range(n)] for _ in range(m)]

Q = deque()
dx = [1,-1,0,0]
dy= [0,0,1,-1]
ch[0][0]=1

Q.append((0,0))

while Q:
    p = Q.popleft()
    for i in range(4):
        a= p[0]+dx[i]
        b = p[1]+dy[i]
        if ch[a][b]==1:
            
