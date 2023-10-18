import sys
import heapq as hq
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

n = int(input())
if n==1:
    print(0)
    sys.exit(0)
L=[]
for i in range(n):
    a=int(input())
    hq.heappush(L,a)
ans =0
while L:
    a=hq.heappop(L)
    b=hq.heappop(L)
    ans+=a+b
    if len(L)==0:
        break
    hq.heappush(L,a+b)

print(ans)