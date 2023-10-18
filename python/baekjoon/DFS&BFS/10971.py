import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
sys.setrecursionlimit(10**6)
n = int(input())

g = [list(map(int,input().split())) for _ in range(n)]
mind = 1000000000
def DFS(L,a,tot):
    global mind, start
    if L==n-1 :
        if g[a][start]>0 and tot+ g[a][start] <mind :
            mind = tot+ g[a][start]
        return
    else:
        for i in range(n):
            if ch[i] ==0 and g[a][i]>0:
                ch[i]=1
                DFS(L+1,i,tot+g[a][i])
                ch[i]=0

ch = [0]*n
for i in range(n):
    start=i
    ch[i]=1
    DFS(0,i,0)
    ch[i]=0

print(mind)