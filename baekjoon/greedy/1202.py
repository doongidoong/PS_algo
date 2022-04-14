import sys
import heapq as hq
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

n,k = map(int,sys.stdin.readline().split())

q = []
for i in range(n):
    m,v= map(int, sys.stdin.readline().split())
    hq.heappush(q,(m,v))

bag=[]
for _ in range(k):
    a= int(input())
    hq.heappush(bag, a)
ans=0
temp=[]
for i in range(k):
    capa = hq.heappop(bag)
    while q and capa >= q[0][0]:
        m,v= hq.heappop(q)
        hq.heappush(temp,-1*v)
    if temp:
        ans-=hq.heappop(temp)
    elif not q:
        break
print(ans)