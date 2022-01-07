import sys
from collections import deque
#sys.stdin = open("input.txt","rt")

a = input()

n = int(input())
L = list( input() for _ in range(n))

for i in range(n):
    dq = deque()
    for j in a:
        dq.append(j)
    cnt =0
    p=0
    while(dq and p<len(L[i])):
        if L[i][p] in dq:
            if L[i][p] ==dq[0]:
                cnt+=1
                str =dq.popleft()
            else:
                break
        p+=1
        if cnt==len(a):
            L[i]='YES'
            break
    

for i in range(n):
    if L[i] == 'YES':
        print("#{} YES".format(i+1))
    else:
        print("#{} NO".format(i+1))
    