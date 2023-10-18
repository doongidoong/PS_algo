#테트로미노
import sys
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")


def DFS(L,x,y,s):
    global answer
    if L==3:
        if s > answer:
            answer = s
        return 
    else:
        for i in range(4):
            xx = x +dx[i]
            yy = y +dy[i] 
            if 0<=xx<n and 0<=yy<m and check[xx][yy] ==0:
                check[xx][yy] =1
                DFS(L+1,xx,yy,s+g[xx][yy])
                check[xx][yy] =0
                

def mountain(x,y):
    a=0;b=0;c=0;d =0
    if x+2<n:
        if y+1 <m:
            a = g[x][y]+g[x+1][y]+g[x+2][y]+g[x+1][y+1]
        if y-1 >= 0:
            b = g[x][y]+g[x+1][y]+g[x+2][y]+g[x+1][y-1]
    if y+2<m:
        if x+1 <n:
            c = g[x][y]+g[x][y+1]+g[x][y+2]+g[x+1][y+1]
        if x-1 >= 0:
            d = g[x][y]+g[x][y+1]+g[x][y+2]+g[x-1][y+1]
    return max(a,b,c,d)
n, m = map(int,input().split())
g = [ list(map(int, input().split())) for _ in range(n)]
check = [ [0 for _ in range(m)] for _ in range(n) ]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
answer = 0
for i in range(n):
    for j in range(m):
        check[i][j] =1 
        DFS(0,i,j,g[i][j])
        check[i][j] = 0 
        answer= max(answer,mountain(i,j))

print(answer)
