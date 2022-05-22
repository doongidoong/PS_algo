import sys


sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")

check = [0]*2000000
def DFS(L,s):
    check[s]=1
    if L==n:
        return
    DFS(L+1,s+a[L])
    DFS(L+1,s)

n= int(input())

a = list(map(int,input().split()))
DFS(0,0)
print(check.index(0))