from cmath import inf
import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
node = int(sys.stdin.readline())
edge = int(sys.stdin.readline())
g= [[inf for _ in range(node+1)] for _ in range(node+1)]

for i in range(node+1):
    g[i][i] =0

for i in range(edge):
    a, b, cost = map(int,sys.stdin.readline().split())
    g[a][b] = min(g[a][b],cost)


for k in range(1,node+1):
    for i in range(1,node+1):
        for j in range(1,node+1):
            g[i][j] = min(g[i][j],g[i][k]+g[k][j])

for i in range(1,node+1):
    for j in range(1,node+1):
        if g[i][j] == inf:
            print(0,end=' ')
        else:
            print(g[i][j],end=' ')
    if i!= node:
        print()