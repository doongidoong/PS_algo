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
    dis[start]= 0 #시작은 0
    hq.heappush(q,(0,start)) #우선순위큐로 거리로 정렬 
    while q:
        dist, now = hq.heappop(q) # 가장 가까운 거리순대로 뽑음(처음은 0을 뽑음)
        if dist>dis[now]: #만약 저장된 거리가 더 짧다면 continue 
            continue
        for i in g[now]: # g[now]와 연결된 요소 확인(처음은 start와 연결된 요소들 모두 갱신)
            cost = dist + i[1] # 지금까지의 거리와 now와 해당 노드의 거리 합치기
            if dis[i[0]] >cost: # 저장되어 있는 거리와 (지금까지 거리 + now와의 거리) 비교 
                dis[i[0]] = cost
                hq.heappush(q,(cost,i[0])) #저장된 거리가 갱신되었다면 우선순위큐도 반영 
dijkstra(start)

for i in range(1,n+1):
    if dis[i]==inf:
        print("INF")
    else:
        print(dis[i])

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