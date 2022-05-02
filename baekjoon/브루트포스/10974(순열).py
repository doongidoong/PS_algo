import sys

sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")

n = int(input())
res = ['']*n
check = [0]*(n+1)
def DFS(L):
    if L==n:
        print(" ".join(res))
        return
    for i in range(1,n+1):
        if check[i]==0:
            res[L]=str(i)
            check[i]=1
            DFS(L+1)
            check[i]=0

DFS(0)