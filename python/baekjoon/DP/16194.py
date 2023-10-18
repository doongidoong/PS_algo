
import sys
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")

n = int(input())
dy = [0]*(n+1)

L = list(map(int,input().split()))
for i in range(n):
    dy[i+1] = L[i]


for i in range(1,n//2+1): # 비교할 수
    for j in range(i+1,n+1): # 저장된 값
        dy[j] = min(dy[j],dy[j-i]+dy[i])
print(dy[-1])
