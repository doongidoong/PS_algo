import sys
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")

input = sys.stdin.readline
#from itertools import permutations
n = int(input())

L= list(map(int,input().split()))


for i in range(n-1,0,-1):
    if L[i-1]>L[i]:
        for j in range(n-1,0,-1):
            if L[i-1]>L[j]:
                L[i-1], L[j] = L[j],L[i-1]
                ans = L[:i]+ sorted(L[i:], reverse=True)
                print(*ans)
                sys.exit(0)
print(-1)

