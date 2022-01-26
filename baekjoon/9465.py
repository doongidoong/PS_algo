import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
k = int(input())
for i in range(k):
    n = int(input())
    dy=[ [0]*(n) for _ in range(2)]
    L = [list(map(int,input().split())) for _ in range(2)]
    for i in range(n):
        if i ==0 :
            dy[0][0] = L[0][0]
            dy[1][0] = L[1][0]
        elif i==1:
            dy[0][1] = L[1][0] +L[0][1]
            dy[1][1] = L[0][0] +L[1][1]
        else: 
            dy[0][i] = max(dy[1][i-2],dy[1][i-1],dy[0][i-2])+L[0][i]
            dy[1][i] = max(dy[0][i-2],dy[0][i-1],dy[1][i-2])+L[1][i]
    print(dy[1][n-1])