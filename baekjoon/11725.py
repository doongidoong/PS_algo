import sys
from collections import deque
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
 
sys.setrecursionlimit(10**6)

n = int(input())

def DFS(v):
    for i in g[v]:
        if visited[i]==0:
            visited[i] = v
            DFS(i)

def BFS(v):
    Q = deque()
    Q.append(v)
    while Q:
        now = Q.popleft()
        for i in g[now]:
            if visited[i] == 0:
                visited[i]=now
                Q.append(i)
    return
g = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]


for i in range(n-1): 
    a, b = map(int, sys.stdin.readline().split()) 
    g[a].append(b)
    g[b].append(a)

DFS(1)
#BFS(1)
for j in range(2,n+1):
    print(visited[j])