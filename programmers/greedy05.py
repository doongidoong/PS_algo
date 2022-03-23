import heapq
def solution(n, costs):
    answer = 0
    g=[[] for _ in range(n)]
    for i in costs:
        g[i[0]].append((i[1],i[2]))
        g[i[1]].append((i[0],i[2])) 
    a =dijkstra(g,0)
    answer =sum(a)
    return answer
def dijkstra(g,start):
    distance = [5000]*(len(g))
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dis,now= heapq.heappop(q)
        if dis > distance[now]:
                continue
        for i in g[now]:
            cost = dis + i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    return distance
            



n=4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n,costs))