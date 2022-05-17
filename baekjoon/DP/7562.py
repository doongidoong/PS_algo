import sys
from collections import deque
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")
T = int(input())
move = [(2,1),(2,-1),(1,2),(1,-2),(-2,1),(-2,-1),(-1,2),(-1,-2)]
for i in range(T):
    Q = deque()
    l = int(input())
    start = list(map(int,input().split()))
    end = list(map(int,input().split()))
    Q.append(start+[0])
    check = [ [0 for _ in range(l)] for _ in range(l)]
    while Q:
        now = Q.popleft()
        if now[0] == end[0] and now[1] == end[1]:
            print(now[2])
            break
        for j in range(8):
            x = now[0]+move[j][0]
            y = now[1]+move[j][1]
            if 0<=x<l and 0<=y<l and check[x][y]==0:
                check[x][y]= 1 
                Q.append([x,y,now[2]+1])
