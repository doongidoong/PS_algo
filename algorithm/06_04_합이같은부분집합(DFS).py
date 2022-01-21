import sys
#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")

def DFS(L,sum):
    if sum>total//2:
        return
    if L == n:
        if sum == (total - sum):
            print("YES")
            sys.exit(0) # 프로그램 종료
    else:
        DFS(L+1, sum + a[L])
        DFS(L+1, sum)

if __name__ == "__main__":
    n = int(input())
    a = list(map(int,input().split()))
    total = sum(a)
    DFS(0,0)
    print("NO") # 프로그램 종료가 안되었다면


# 내풀이
"""
n = int(input())
ch =[0]*(n)

L = list(map(int,input().split()))
check = [0]
def dfs(v):
    if v==n:
        sumL=sum(L)
        for i in range(n):
            if ch[i] == 1:
                sumL-=L[i]
        if sum(L)-sumL == sumL:
            check[0]=1
        return 
    else:
       ch[v]=1
       dfs(v+1)
       ch[v]=0
       dfs(v+1)
dfs(1)

if check[0]==1:
    print("YES")
else:
    print("NO")



"""