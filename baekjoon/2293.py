from cmath import inf
import sys
from collections import defaultdict
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

n,k= map(int,sys.stdin.readline().rstrip().split())

coin = [int(sys.stdin.readline()) for _ in range(n)]

dy = [0]*(k+1)
dy[0]=1
for c in coin:
    for i in range(1,k+1):
        if i-c>=0 :
            dy[i]+=dy[i-c]
print(dy)
