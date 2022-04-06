from collections import defaultdict
answer = []
graph = defaultdict(list)
check = defaultdict(int)

def solution(tickets):
    for a,b in tickets:
        graph[a].append(b)
        check[a+b]=-1
    for a, b in graph.items():
        graph[a].sort()
    DFS("ICN")
    print(check)
    return answer[::-1]
def DFS(now):
    for i in graph[now]:
        if check[now+i] !=0:
            check[now+i] += 1
            DFS(i)
            check[now+i] -= 1
    answer.append(now)
    



tickets= [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
print(solution(tickets))

