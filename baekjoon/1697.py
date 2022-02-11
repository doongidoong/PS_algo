from cmath import inf
import sys
from collections import deque
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n,k = map(int ,input().split())

Q  = deque()

Q.append(n)
maxrange=100000
dy = [inf]*(maxrange+1)
dy[n]=0
while Q :
    p = Q.popleft()
    if p-1>=0 and dy[p-1] > dy[p]+1:
        dy[p-1] = dy[p]+1
        Q.append(p-1)
    if p+1<=maxrange and dy[p+1] > dy[p]+1:
        dy[p+1] =dy[p]+1
        Q.append(p+1)
    if 2*p<=maxrange and dy[2*p]>dy[p]+1: 
        dy[p*2] =dy[p]+1
        Q.append(p*2)
    if p==k:
        break
print(dy[k])