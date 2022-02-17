import sys
from collections import defaultdict

sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n = int(input())
a=int(input())
A=list(map(int,input().split()))

b=int(input())
B=list(map(int,input().split()))

left = defaultdict(int)
right = defaultdict(int)

for i in range(a):
    for j in range(i,a):
        left[sum(A[i:j+1])] += 1

ans=0
for i in range(b):
    for j in range(i,b):
        ans += left[n - sum(B[i:j+1])]

print(ans)