import sys
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\samsung\\input.txt","r")

n  = int(input())
timeList = []
moneyList = []
dp = [0]*n
for i in range(n):
    t, m = map(int, input().split())
    timeList.append(t)
    if i+t<=n:
        moneyList.append(m)
    else:
        moneyList.append(0)
for i in range(n):
    maxMoney = 0    
    for j in range(i):
        if j+ timeList[j]<=i:
            maxMoney = max(maxMoney, dp[j])
    dp[i] = max(dp[i], maxMoney + moneyList[i])

print(max(dp))
    
