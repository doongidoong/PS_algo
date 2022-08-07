from collections import deque
checked = []
wireGraph = []

r =0
def solution(n, wires):
    global checked, wireGraph, r
    answer = n
    for k in range(len(wires)):
        wireGraph = [[0 for _ in range(n+1)] for _ in range(n+1)]
        checked = [0 for _ in range(n+1)] 
        for j in range(len(wires)):
            if k==j:
                continue
            a,b = wires[j]
            wireGraph[a][b] = 1
            wireGraph[b][a] = 1
        checked[1]=1
        visit = set()
        visit.add(1)
        r= DFS(visit,1,n)
        answer = min(answer, abs(n-2*r))
    return answer
def DFS(visit, now,n):
    for i in range(1,n+1):
        if wireGraph[now][i] and checked[i] ==0 :
            visit.add(i)
            checked[i]=1
            DFS(visit,i,n)
            checked[i]=0
    return len(visit)



n= 4
wires = [[1,2],[2,3],[3,4]]
print(solution(n,wires))