import sys
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")
T = int(input())

dy = [[0,0,0] for _ in range(100001)]

dy[1]=[1,0,0]
dy[2]=[0,1,0]
dy[3]=[1,1,1]

for i in range(4,100001):
    dy[i][0] = (dy[i-1][1]+dy[i-1][2]) %1000000009
    dy[i][1] = (dy[i-2][0]+dy[i-2][2]) %1000000009
    dy[i][2] = (dy[i-3][0]+dy[i-3][1]) %1000000009

for i in range(T):
    n = int(input())
    k = dy[n][0]+ dy[n][1]+dy[n][2]
    print(k%1000000009)

