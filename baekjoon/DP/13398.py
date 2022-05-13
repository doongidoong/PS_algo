import sys
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")

n = int(input())
L = list(map(int,input().split()))

dp = [0 for _ in range(n)]
dp2 = [0 for _ in range(n)]
k=0
dp[0]= L[0]

for i in range(1,n):
    dp[i] = max(dp[i-1]+L[i],L[i])
    dp2[i] = max(dp2[i-1]+L[i],L[i])    
    if dp2[i] < dp[i-1]:
        dp2[i]= dp[i-1]

ret= max(max(dp),max(dp2))
if ret==0:
    print(max(L))
else:
    print(ret)