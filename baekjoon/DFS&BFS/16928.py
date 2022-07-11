import sys
from collections import deque
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\baekjoon\\input.txt","rt")


n, m = map(int, sys.stdin.readline().split())

# 보드판을 표현, 사다리나 뱀인 경우에는 이동 후 좌표로 표시
graph = [i for i in range(101)]
for _ in range(n + m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a] = b

visited = [0] * 101

# bfs 탐색

queue = deque([1])
visited[1] = 1

while queue:
    q = queue.popleft()
    if q >= 100:
        print(visited[q]-1)
        break
    for i in range(1,7):
        now = q+i
        if now<= 100:
            if graph[now] > 0:
                now = graph[now]
            if not visited[now]:
                visited[now] =  visited[q]+1
                queue.append(now)
