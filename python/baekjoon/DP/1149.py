import sys
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")

n = int(input())

L = [ list(map(int, input().split())) for _ in range(n) ] 


for i in range(1,n):
    L[i][0] += min(L[i-1][1],L[i-1][2])
    
    L[i][1] += min(L[i-1][0],L[i-1][2])
    
    L[i][2] += min(L[i-1][0],L[i-1][1])

print(min(L[n-1]))