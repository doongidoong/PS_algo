import sys
from collections import deque
Q = deque()
#sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")
n,k = map(int, input().split())
path = [0]*100001
dist = [0]*100001
Q.append(n)
while Q:
    now = Q.popleft()
    if now==k:
        print(dist[now])
        arr = []
        temp = now
        for _ in range(dist[now]+1):
            arr.append(temp)
            temp = path[temp]
        print(' '.join(map(str, arr[::-1])))
        break
    for i in (now+1, now-1, 2*now):
        if 0<=i<=100000 and dist[i]==0:
            Q.append(i)
            dist[i] = dist[now] + 1
            path[i] = now