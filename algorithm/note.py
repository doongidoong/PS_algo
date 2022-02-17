from cmath import inf
import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

v,e = map(int,input().split())
start = int(input())
g=[[] for _ in range(v+1)]
visited =[0]*(v+1) 
dis =[inf]*(v+1)
for i in range(e):
    a,b,c = map(int,input().split())
    g[a].append((b,c))

def get_smallest():
    minval = inf
    index = 0
    for i in range(1,v+1):
        if dis[i] < minval and not visited[i] :
            minval = dis[i]
            index= i
    return index

def dijkstra(start):
    dis[start] =0
    visited[start] =1 
    for i in g[start]:
        dis[i[0]] = i[1]
    for i in range(v-1):
        now = get_smallest()
        visited[now] =1 
        for j in g[now]:
            dis[j[0]] = min(dis[j[0]], dis[now]+j[1])

dijkstra(start)

print(dis)