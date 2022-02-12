import sys
from collections import deque


#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

a,b,c = map(int,input().split())

Q=deque()

Q.append((0,0))
d = [[0 for _ in range(b+1)] for _ in range(a+1)]
dy = []
d[0][0]=1
while Q:
    p1, p2 = Q.popleft()
    p3 = c-p1-p2
    if p1==0:
        dy.append(p3)
    if p1>0 and p2 <b:
        t = min(p1,b-p2)
        if d[p1-t][p2+t]==0:
            d[p1-t][p2+t]=1
            Q.append((p1-t,p2+t))
    if p1>0 and p3 <c:
        t = min(p1,c-p3)
        if d[p1-t][p2]==0:
            d[p1-t][p2]=1
            Q.append((p1-t,p2))
    if p2>0 and p1 <a:
        t = min(p2,a-p1)
        if d[p1+t][p2-t]==0:
            d[p1+t][p2-t]=1
            Q.append((p1+t,p2-t))
    if p2>0 and p3 <c:
        t = min(p2,c-p3)
        if d[p1][p2-t]==0:
            d[p1][p2-t]=1
            Q.append((p1,p2-t))
    if p3>0 and p1 <a:
        t = min(p3,a-p1)
        if d[p1+t][p2]==0:
            d[p1+t][p2]=1
            Q.append((p1+t,p2))
    if p3>0 and p2 <b:
        t = min(p3,b-p2)
        if d[p1][p2+t]==0:
            d[p1][p2+t]=1
            Q.append((p1,p2+t))
dy = set(dy)
dy = list(dy)
dy.sort()
print(' '.join(list(map(str, dy))))