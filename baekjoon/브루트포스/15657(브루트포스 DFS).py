import sys

sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")
n,m = map(int, input().split())
a = list(map(int,input().split()))
t=[0]*(m)
a.sort()
check = [0]*(n)
def DFS(L,s,k):
    if L==m:
        for i in t:
            print(i,end=' ')
        print()
        return
    for i in range(n):
        if k <= a[i]:
            t[L]=a[i]
            DFS(L+1,i+1,a[i])
        
DFS(0,0,0)
