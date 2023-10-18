import sys
from collections import deque
from itertools import combinations

sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\samsung\\input.txt","r")

n,m  = map(int, input().split())
board = [ list(map(int,input().split())) for _ in range(n)]
allCase= []
start = []
q = deque()
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            allCase.append([i,j])
        elif board[i][j] == 2:
            start.append([i,j])
combi = list(combinations(allCase,3))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

lenAll = len(allCase)
answer = 0
for c in combi:
    c = list(c)
    for j in range(len(c)):
        board[c[j][0]][c[j][1]] = 1
    q = deque()
    totalCnt = 0
    for s in start:
        q.append(s)
    check = [ [0]*m for _ in range(n)]
    while q:
        nowX, nowY = q.popleft()
        for i in range(4):
            xx = nowX+dx[i]
            yy = nowY+dy[i]
            if 0<=xx<n and 0<=yy<m and check[xx][yy] == 0 and board[xx][yy] == 0:    
                check[xx][yy] = 1
                totalCnt+=1
                q.append([xx,yy])
    
    answer = max(answer, lenAll- totalCnt-3)
    for j in range(len(c)):
        board[c[j][0]][c[j][1]] = 0
            

print(answer)