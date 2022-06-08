import sys
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")
n,m = map(int,input().split())
L = list(map(int,input().split()))
dp =[0]*(len(L)+1)
temp = L[0]
dp[1]= temp

for i in range(1,len(L)):
    temp +=L[i]
    dp[i+1] = temp

for i in range(m):
    a,b = map(int,input().split())
    print(dp[b]-dp[a-1])
