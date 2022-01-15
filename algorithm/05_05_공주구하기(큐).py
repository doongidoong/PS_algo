import sys
from collections import deque
#sys.stdin =  open("input.txt", "rt")

a,k = map(int,input().split())

que = deque()
i =0

for i in range(1,a+1):
    que.append(i)

cnt =1
while que:
    for _ in range(k-1):
        cur = que.popleft()
        que.append(cur)
    que.popleft()
    if len(que)==1:
        print(que[0])
        que.popleft()
