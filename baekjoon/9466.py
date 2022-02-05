import sys
from collections import deque
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    A = [0] + list(map(int,input().split()))
    ind = [0 for _ in range(N+1)]
    for i in range(1,N+1):
        ind[A[i]] += 1
    Q = deque()
    print(ind)
    for i in range(1,N+1):
        if ind[i]==0:
            Q.append(i)
    print(Q)
    while Q:
        cur = Q.popleft()
        next = A[cur]
        ind[next] -= 1
        if ind[next]==0:
            Q.append(next)
    ans = 0
    for i in range(1,N+1):
        if ind[i]==0:
            ans += 1
    print(ans)

"""
t = int(input())
for s in range(t):
    n = int(input())
    a= list(map(int,sys.stdin.readline().split()))
    g = [[] for _ in range(n+1)]
    for i in range(n):
        g[i+1].append(a[i])

    ch = [0 for _ in range(n+1)]
    res = 0

    for i in range(1,n+1):
        if ch[i]==0:
            d = {}
            k = 1
            Q = deque()
            ch[i]=1
            Q.append(i)
            while Q:
                p = Q.popleft()
                d[p] = k
                if ch[g[p][0]]==0:
                    ch[g[p][0]]=1
                    Q.append(g[p][0])
                else :
                    if d.get(g[p][0],0) > 0:
                        res +=  d.get(g[p][0],0)-1
                        break
                    else:
                        res +=k
                k+=1
    print(res)
"""