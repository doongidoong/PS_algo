import sys
sys.stdin = open("input.txt","rt")

n, m = map(int ,input().split()) #n은 노드의 개수 m은 간선의 개수

g = [[0]*(n+1) for _ in range(n+1)]


for i in range(m):
    a,b=  map(int ,input().split())
    g[a][b] =1
    g[b][a] =1


for i in range(1,n+1):
    for j in range(1,n+1):
        print(g[i][j],end=' ')
    print() 