from cmath import inf
import heapq
from collections import deque
def solution(n, edge):
    answer = 0
    g=[[] for _ in range(n+1)]
    for i in edge:
        g[i[0]].append(i[1])
        g[i[1]].append(i[0])
    answer = 0
    dis =[0 for _ in range(n+1)]
    dis[1] = 1
    Q = deque()
    Q.append((1,1))
    while Q:
        p = Q.popleft()
        for i in g[p[0]]:
            if dis[i]==0:
                dis[i]=p[1]+1
                Q.append((i,dis[i]))
    answer=0    
    maxd = max(dis)
    for i in range(2,n+1):
        if maxd==dis[i]:
            answer+=1
    print(answer)
    return answer


n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

solution(6,vertex)