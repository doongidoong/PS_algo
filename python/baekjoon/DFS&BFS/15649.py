import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

n, m = map(int,input().split())
res =[0]*m
ch = [0]*(n+1)
def dfs(L,s):
    if L==m:
        for r in res:
            print(r, end=' ')
        print()
    else:
        for i in range(s,n+1):
            res[L]=i
            dfs(L+1,i)
               
dfs(0,1)