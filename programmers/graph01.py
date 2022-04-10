from cmath import inf
import heapq
def solution(n, edge):
    answer = 0
    return answer

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
n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

print(vertex)