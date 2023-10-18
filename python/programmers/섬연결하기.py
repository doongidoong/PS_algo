import heapq
def solution(n, costs):
    g=[[] for _ in range(n)]
    for i in costs:
        g[i[0]].append((i[1],i[2]))
        g[i[1]].append((i[0],i[2])) 
    answer =prim(g,0)
    return answer

def prim(g,start):
    visited = [0]*(len(g))
    q=[]
    heapq.heappush(q,(0,start))
    total_weight = 0 # 전체 가중치
    while q:
        weight,now= heapq.heappop(q)
        if visited[now]==1:
                continue
        visited[now]=1 
        total_weight+=weight
        for i in g[now]:
            heapq.heappush(q,(i[1],i[0]))# 일단 다 넣고 어차피 visited에서 걸러진다.
    return total_weight