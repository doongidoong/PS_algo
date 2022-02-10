import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n =int(input())
a= [ list(map(int,input().split())) for _ in range(n)]
res = [0]*n
mind=100000000000
def DFS(L,s,tot):
    global mind
    if tot>mind:
        return
    if L==n:
        if tot<mind:
            mind = tot
    else:
        for i in range(3):
            if i !=s:
                res[L] =i
                DFS(L+1,i,tot+a[L][i])

DFS(0,-1,0)

print(mind)