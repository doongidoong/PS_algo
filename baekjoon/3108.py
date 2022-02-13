import sys
from collections import deque
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

n = int(input())

g = []
visit =[0]*(n+1)
collision = [1]*(n+1)
g.append((0,0,0,0))
for i in range(n):
    x1, y1, x2, y2 = map(int,input().split())
    g.append((x1, y1, x2, y2 ))
g.sort()
Q = deque()

def check(a,b):
    #case1
    if g[a][0] < g[b][0] < g[a][2] and g[a][1] < g[b][1] < g[a][3]  and g[a][0] < g[b][2] < g[a][2] and g[a][1] < g[b][3] < g[a][3]   :
        return 1
    elif g[a][2] < g[b][0] and g[a][2] < g[b][2]:
        return 1
    elif g[a][3] < g[b][1] and g[a][3] < g[b][3]:
        return 1
    elif g[a][0] > g[b][0] and g[a][0] >g[b][2]:
        return 1
    elif g[a][1] > g[b][1] and g[a][1] >g[b][3]:
        return 1
    else:
        return 0


Q.append(0)
visit[0]=1
while Q:
    p =Q.popleft()
    ch=0
    for i in range(p+1,n+1):
        if check(p,i)==0 and visit[i]==0:
            visit[i]=1
            collision[i]=0
            Q.append(i)
            ch=1
    if ch ==0:
        for i in range(n):
            if visit[i]==0:
                visit[i]=1
                Q.append(i)
                break
print(sum(collision)-1) 
