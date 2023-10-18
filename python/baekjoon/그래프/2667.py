import sys
from collections import deque
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")

n =int(input())
L = [list(map(int,input())) for _ in range(n)]

count =[]
dx =[0,0,1,-1]
dy =[1,-1,0,0]
Q=deque()

for i in range(n):
    for j in range(n):
        if L[i][j]==1:
            Q.append((i,j))
            L[i][j]=0
            cnt=0
            while Q:
                cnt+=1
                x,y = Q.popleft()
                for t in range(4):
                    xx= dx[t]+x
                    yy = dy[t]+y
                    if 0<=xx<n and 0<= yy<n and L[xx][yy]==1:
                        Q.append((xx,yy))
                        L[xx][yy]=0
            count.append(cnt)
count.sort()
print(len(count))
for i in count:
    print(i)