import sys
from collections import deque
sys.stdin =  open("input.txt", "rt")

n,m = map(int,input().split())

Q  = [(pos, value) for pos, value in enumerate(list((map(int, input().split()))))]

Q =deque(Q)
cnt =0

while 1:
    cur = Q.popleft()
    if any(cur[1]<x[1] for x in Q):
        Q.append(cur)
    else:
        cnt+=1
        if cur[0] == m:
            print(cnt)
            break


""" 
dq = deque(map(int, input().split()))
cur=m
order =0
while dq:
    num = dq.popleft()
    if len(dq)==0:
        print(order+1)
        break
    else:
        if max(dq)<=num:
            order+=1
            if cur == 0 :
                print(order)
                break
        else:
            dq.append(num)
            if cur == 0:
                cur =len(dq)
    cur -=1
"""