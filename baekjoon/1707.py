import sys
from collections import deque
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")


k= int(input())
for j in range(k):
    n,m = map(int,input().split())
    g = [[] for _ in range(n+1)]
    for i in range(m):
        a,b =map(int,input().split())
        g[a].append(b)
        g[b].append(a)
    ch=[0 for _ in range(n+1)]
    Q =deque()
    k=1
    check=0
    for i in range(1,n+1):
        if ch[i]==0 and check==0:
            Q.append(i)
            ch[i]=1
            while Q:
                a = Q.popleft()
                for i in g[a]:
                    if ch[i] == 0:
                        ch[i] = -ch[a]
                        Q.append(i)
                    else:
                        if ch[i] == ch[a]:
                            check=1
                            break
    if check==0:
        print("YES")
    else:
        print("NO")
    check=0
