from cmath import inf
import sys
import heapq as hq

sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n,e = map(int,input().split())
start = int(input())
g=[[] for _ in range(n+1)]

for i in range(e):
    a,b,c = map(int,input().split())
    g[a].append((b,c))

dis = [inf]*(n+1)
    
def dijkstra(start):
    q= []
    dis[start]= 0
    hq.heappush(q,(0,start))
    while q:
        dist, now = hq.heappop(q)
        if dist>dis[now]:
            continue
        for i in g[now]:
            cost = dist + i[1]
            if dis[i[0]] >cost:
                dis[i[0]] = cost
                hq.heappush(q,(cost,i[0]))



dijkstra(start)
"""
v,e = map(int,input().split())
start = int(input())
g=[[] for _ in range(v+1)]
dis =[inf]*(v+1)
for i in range(e):
    a,b,c = map(int,input().split())
    g[a].append((b,c))

def dijkstra(start):
    q=[]
    hq.heappush(q,(0,start))
    dis[start] =0
    while q:
        dist, now = hq.heappop(q)
        if dist > dis[now]:
            continue   
        for j in g[now]:
            cost = dist + j[1]
            if cost < dis[j[0]] :
                dis[j[0]] = cost
                hq.heappush(q,(cost,j[0]))

dijkstra(start)
"""
for i in range(1,n+1):
    if dis[i]==inf:
        print("INF")
    else:
        print(dis[i])