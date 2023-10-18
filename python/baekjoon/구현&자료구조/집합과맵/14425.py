import sys
from collections import defaultdict



sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")
a,b = map(int,input().split())
d= defaultdict(int)

for i in range(a):
    s = input()
    d[s] =1

ans = 0
for i in range(b):
    s = input()
    if d[s] >0:
        ans+=1

print(ans) 
