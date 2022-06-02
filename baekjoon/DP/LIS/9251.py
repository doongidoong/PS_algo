import sys
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")
    
s1 = input()
s2 = input()

dp= [0]*10
ind =[-1]*10

for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i]==s2[j] and ind[j]<i:
            ind[j] =i
            dp[j]+=1
    print('ind=',ind)
    print(dp)
print(max(dp))