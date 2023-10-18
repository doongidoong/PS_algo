import sys

sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")

n = int(input())
L = list(map(int,input().split()))

dp = [0 for i in range(n)]

dp[0] = L[0]
for i in range(1,n):
    dp[i] = max(dp[i-1],0)+L[i]

print(max(dp))
