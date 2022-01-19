import sys

sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")
n,m = map(int, input().split())
board = board=[list(map(int, input().split())) for _ in range(n)]


def dfs(L,j):
    if L==m:
        for r in res:
            ps[r] 

        return
    else:
        for i in range(j,len(ps)):
            if ch[i]==0:
                ch[i]=1
                res[L]=i
                dfs(L+1,i+1)
                ch[i]=0

hs =[]
ps = []
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            hs.append((i,j))
        elif board[i][j]==2:
            ps.append((i,j))
ch = [0]*len(ps)
res = [0]*m
dfs(0,0)