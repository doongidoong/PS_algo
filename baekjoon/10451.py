import sys
from collections import deque
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

Q = deque()

t = int(input())
for _ in range(t):
    n = int(input())
    a= list(map(int, input().split()))
    g = [[] for _ in range(n+1)]
    cnt = 0
    for i in range(1,n+1):
        g[i].append(a[i-1])
    ch=[0 for _ in range(n+1)]
    for i in range(1,n+1):
        if ch[i]==0:
            Q.append(i)
            ch[i] = 1
            while Q:
                p= Q.popleft()
                for j in g[p]:
                    if ch[j]==0:
                        Q.append(j)
                        ch[j]=1
            cnt+=1       
    print(cnt) 