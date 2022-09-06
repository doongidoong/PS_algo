import heapq
from pickle import FALSE

# 1. 출입로를 반드시 포함
# 2. 산봉우리를 반드시 포함
# 3. 사이클 발생

def solution(n, paths, gates, summits):
    answer = []
    graph = [[] for i in range(n+1)]
    for path in paths:
        a, b = path[0],path[1]
        weight = path[2]
        graph[a].append((weight,b))
        graph[b].append((weight,a))
    for summit in summits:
        graph[summit] = []
    h = [[0,gate] for gate in gates]
    dp = [float('inf') for i in range(n+1)]
    for gate in gates:
        dp[gate] = 0 
    maxWeight = 0
    heapq.heapify(h)
    while h:
        p = heapq.heappop(h)
        weight = p[0]
        now = p[1]
        if weight > maxWeight:
            maxWeight = weight
        if now in summits or weight > dp[now]:
            continue
        for weight, nextPoint in graph[now]:
            m = max(weight,dp[now])
            if dp[nextPoint] > m :
                dp[nextPoint] = m
                heapq.heappush(h,[m,nextPoint])
    for i in summits:
        if len(answer) == 0 :
            answer = [i,dp[i]]
        elif answer[1] > dp[i] :
            answer = [i,dp[i]]
        elif answer[1] == dp[i] and answer[0] > i :
            answer = [i,dp[i]]
    return answer

print(solution(		6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
