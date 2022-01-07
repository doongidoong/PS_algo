
import sys
import heapq as hq
#sys.stdin = open("input.txt","rt")
a = [] #파이썬은 리스트를 사용하고 여기에 heappush heapop 해주면 됨

while True:
    n = int(input())
    if n ==-1:
        break
    if n==0:
        if len(a)==0:
            print(-1)
        else:
            print(hq.heappop(a)) # 루트 노드를 꺼냄
    else:
        hq.heappush(a , n)

        
