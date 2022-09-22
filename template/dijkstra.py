from cmath import inf
import heapq  # 우선순위 큐 구현을 위함
graph1 = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
graph2 = [[],[],[],[],[]]


def dijkstra(n,graph, start):
    distances  = [ inf for _ in range(n)] 
    distances[start] = 0  # 시작 값은 0이어야 함
    queue = []
    heapq.heappush(queue, (distances[start], start))  
    while queue:  # queue에 남아 있는 노드가 없으면 끝
        current_distance, current_destination = heapq.heappop(queue)  
        if distances[current_destination] < current_distance: 
            continue
        for new_destination in range(n):
            new_distance = graph[current_destination][new_destination]
            distance = current_distance + new_distance  
            if distance < distances[new_destination]:  
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])  
    return distances


def dijkstra2(graph, start):
    dis = [float('inf')]*(len(graph)+1)
    q=[]
    heapq.heappush(q,(0,start))
    dis[start] = 0
    while q:
        distance, now  = heapq.heappop(q)
        if distance > dis[now]:
            continue
        for i in graph[now]:
            cost = distance + i[1]
            if dis[i[0]] > cost:
                dis[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return dis
