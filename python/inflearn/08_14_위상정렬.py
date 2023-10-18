import sys
from collections import deque
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")

n, m = map(int,input().split())
degree= [0]*(n+1)
g = [[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    a, b = map(int,input().split())
    degree[b] +=1 
    g[a][b] =1 


Q = deque()

"""내풀이
while sum(degree)!=-1*n:
    for k in range(1,n+1):
        if degree[k] == 0:
            Q.append(k)
    while Q:
        p = Q.popleft()
        print(p,end=' ')
        degree[p]-=1
        for i in range(1,n+1):
            if g[p][i] == 1 :
                degree[i] -=1
"""
for k in range(1,n+1):
    if degree[k] == 0:
        Q.append(k)
while Q:
    p = Q.popleft()
    print(p,end=' ')
    for i in range(1,n+1):
        if g[p][i] == 1 :
            degree[i] -=1
            if degree[i] == 0:
                Q.append(i)
        