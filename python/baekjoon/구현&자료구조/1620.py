import sys
from collections import defaultdict

sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")
    
n,m = map(int, sys.stdin.readline().rstrip().split())

d ={}


for i in range(1,n+1):
    s = sys.stdin.readline().rstrip()
    d[s] = i
    d[str(i)] = s


for j in range(m):
    k = sys.stdin.readline().rstrip()
    print(d[k])

