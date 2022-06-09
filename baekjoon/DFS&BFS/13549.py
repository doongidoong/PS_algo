from cmath import inf
import sys
import heapq 

sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")
n,k = map(int, input().split())
Q = [] 

heapq.heappush(Q,(0,n))
dist = [inf]*200001
    while Q:
    now = heapq.heappop(Q)
    if now[1]==k:
        print(now[0])
        break    
    if 2*now[1] <= 2*k and now[0]<dist[2*now[1]]:
        dist[2*now[1]] =now[0]
        heapq.heappush(Q,(now[0],2*now[1]))
    for i in (now[1]+1, now[1]-1):
        if 0<=i<=200001 and now[0]+1<dist[i]:
            dist[i] =now[0]+1
            heapq.heappush(Q,(now[0]+1,i))

