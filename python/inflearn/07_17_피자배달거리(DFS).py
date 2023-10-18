import sys

#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")
n,m = map(int, input().split())
board =[list(map(int, input().split())) for _ in range(n)]

tot=[]
def dfs(L,s):
    if L==m:
        sum =0
        for h in hs:
            dis = n*n
            for c in cb:
                x = h[0]-ps[c][0]
                y = h[1]-ps[c][1]
                dis = min(dis,abs(x)+abs(y))
            sum+=dis
        tot.append(sum)
        return
    else:
        for i in range(s,len(ps)):
            cb[L]=i
            dfs(L+1,i+1)
                
hs =[]
ps = []
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            hs.append((i,j))
        elif board[i][j]==2:
            ps.append((i,j))
ch = [0]*len(ps)
cb = [0]*m
dfs(0,0)

print(min(tot))