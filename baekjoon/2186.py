import sys

#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n,m,k = map(int,input().split())
g = [ list(input()) for _ in range(n)]
answer = list(input()) 

move= []

target= len(answer)


dp = [[ [ -1]*len(answer) for _ in range(m)] for _ in range(n) ] 

def DFS(L,x,y):
    if dp[x][y][L]!=-1:
        return dp[x][y][L]
    if g[x][y] != answer[L]:
        return 0
    if L>=target-1:
        return 1
    res= 0
    for i in range(-k,k+1):
        if i ==0 :
            continue
        if 0<=x+i<=n-1 :
            res += DFS(L+1,x+i,y)
        if 0<=y+i<=m-1:
            res += DFS(L+1,x,y+i)
    dp[x][y][L] = res
    return res
t =0
for i in range(n):
    for j in range(m):
        if g[i][j] == answer[0]:
            t+=DFS(0,i,j)
print(t)