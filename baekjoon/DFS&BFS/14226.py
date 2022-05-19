import sys
from collections import deque
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")
start = [1,0]
s = int(input())
Q = deque()

Q.append(start)
# 1, 2, 4, 8, 16, 32 64, 128
dis = [0]*100000

while Q:
    now = Q.popleft()
    screen = now[0]
    board = now[1]
    k=0
    if screen ==board:
        k=1
    if screen==s:
        print(dis[screen])
        break
    if screen != board:
        Q.append([screen,screen])
    if screen+board <= 10000 and dis[screen+board]==0:
        dis[screen+board] = dis[screen]+1+k
        Q.append([screen+board,board])
    if screen -1>=0 and dis[screen-1]==0:
        dis[screen-1] = dis[screen]+1+k
        Q.append([screen-1,board])
    
