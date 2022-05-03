import sys
#sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")

input = sys.stdin.readline
n = int(input())
data = list(map(int,input().split()))

for i in range(n-1,0,-1):
    if data[i-1]<data[i]:
        for j in range(n-1,0,-1):
            if data[i-1]<data[j]:
               data[i-1], data[j] =data[j],data[i-1]
               ans = data[:i] + sorted(data[i:])
               print(*ans)
               sys.exit(0)

print(-1)