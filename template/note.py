from collections import deque
def solution(info, edges):
    answer = 0
    graph = [[] for _ in range(len(info))]
    max_sheep = 0
    for edge in edges:
        graph[edge[0]].append(edge[1])
    q = deque()
    q.append((0,1,0,set()))
    while q:
        now,sCnt,wCnt, nextNode =q.popleft()
        max_sheep = max(max_sheep,sCnt)
        for i in graph[now]:
            nextNode.add(i)
        for next in nextNode:
            if info[next]: # wolf
                if sCnt > wCnt+1 :
                    q.append((next,sCnt,wCnt+1,nextNode - {next}))
            else:
                q.append((next,sCnt+1,wCnt,nextNode- {next}))
    return max_sheep