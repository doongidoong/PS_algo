import sys
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")
m = list(input())
n = list(input())
l1 = len(m)
l2 = len(n)
dp = [[0] * (l2 + 1) for i in range(l1 + 1)]
for i in range(l1):
    for j in range(l2):
        if m[i] == n[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
print(dp[l1][l2])