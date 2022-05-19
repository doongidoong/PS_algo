import sys
from collections import deque

sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")
start = (1,0)
s = int(input())
Q = deque()

Q.append(start)
# 1, 2, 4, 8, 16, 32 64, 128
dis = [[0]*(1001) for _ in range(1001)]

while Q:
    now = Q.popleft()
    screen = now[0]
    board = now[1]
    d = dis[screen][board]
    if screen == s:
        print(d)
        break 
    if dis[screen][screen]==0:
       dis[screen][screen]=d+1
       Q.append((screen,screen))
    if screen+board <= s and dis[screen+board][board]==0:
       dis[screen+board][board]=d+1
       Q.append((screen+board,board))
    if screen-1 >=0 and dis[screen-1][board]==0:
       dis[screen-1][board]=d+1
       Q.append((screen-1,board))
    