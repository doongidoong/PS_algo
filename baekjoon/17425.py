import sys
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")

n = [ 1]*(1000001)
s =[ 0]*(1000001)
for i in range(2,1000001):
    for j in range(i,1000001,i):
        n[j]+=i
for i in range(1, 1000001):
    s[i] = s[i-1] + n[i]
t = int(input())
for i in range(t):
    num = int(input())
    print(s[num])