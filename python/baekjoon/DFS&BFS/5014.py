from cmath import inf
import sys
from collections import deque
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

F, S, G, U, D = map(int,input().split())
Q=deque()
visit = [0]*(F+1)
dis = [inf]*(F+1)
#upcase
start = S
visit[S]= 1
dis[S]=0
if S<G and U > 0:
    move = (G-S)//U
    start = move*U + S
    dis[start]=move
#downcase
if S>G and D != 0: 
    move = (S-G)//D
    start = S- move*D
    dis[start]=move

visit[start]=1
Q.append(start)

while Q:
    p = Q.popleft()
    if p == G:
        print(dis[p])
        break
    if p + U <= F and visit[p + U]==0:
        visit[p+U]=1
        dis[p+U] = min(dis[p+U] ,dis[p]+1)
        Q.append(p + U)
    if p - D >= 1 and visit[p - D ]==0:
        visit[p - D] =1
        dis[p-D] = min(dis[p-D] ,dis[p]+1)
        Q.append(p - D)
else:
    print("use the stairs")