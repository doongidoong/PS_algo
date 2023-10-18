from cmath import inf
import heapq as hq


def solution(n, s, a, b, fares):
    answer  = 0
    g=[[] for _ in range(n+1)]

    for i in range(fares):
        a,b,c = map(int,input().split())
        g[a].append((b,c))
        g[b].append((a,c))
        
    return answer

#시작점으로부터, 모든 노드의 최소 거리를 구함
def dijkstra(start, n,g):
    dist = [ inf for _ in range(n+1)]
    dist[start] = 0
    q= []
    hq.heappush(q,(0,start))
    while q:
        distance, node = hq.heappop(q)
        if dist[node] < distance:
            continue
        for point, cost in g[node]:
            totCost = cost + distance
            if totCost < dist[point]:
                dist[point] = totCost
                hq.heappush(q,(totCost,point))
    return dist






solution( 6	, 4	, 6	, 2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])