from cmath import inf
import sys
import heapq 

sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n,e = map(int,input().split())

g=[[] for _ in range(n+1)]

for i in range(e):
    a,b,c = map(int,input().split())
    g[a].append((b,c))
    g[b].append((a,c))

v1,v2 =  map(int,input().split())

def dijkstra(start):
    dis = [inf]*(n+1)
    q=[]
    heapq.heappush(q,(0,start))
    dis[start] = 0
    while q:
        distance, now  = heapq.heappop(q)
        if distance > dis[now]:
            continue
        for i in g[now]:
            cost = distance + i[1]
            if dis[i[0]] > cost:
                dis[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return dis

original_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

v1_path = original_distance[v1] + v1_distance[v2] + v2_distance[n]
v2_path = original_distance[v2] + v2_distance[v1] + v1_distance[n]
result = min(v1_path, v2_path)
print(result if result < inf else -1)