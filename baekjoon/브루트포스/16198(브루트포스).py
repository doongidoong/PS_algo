import sys


sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")
n= int(input())
a  = list(map(int, input().split()))
visit = [0]*n

answer = 0
def DFS(L,now):
    global answer
    if L==n-2:
        answer = max(answer, now)
        return
    for i in range(1,n-1):
        if visit[i]==0:
            visit[i]=1
            right = 0
            left = 0
            for k in range(i+1,n):
                if visit[k]==0:
                    right=a[k]
                    break
            for k in range(i-1,-1,-1):
                if visit[k]==0:
                    left=a[k]
                    break

            DFS(L+1,now+(right*left))
            visit[i]=0


DFS(0,0)
print(answer)