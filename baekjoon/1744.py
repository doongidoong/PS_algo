from collections import deque
import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n=int(input())
pn =[]
mn =[]
r=0
for i in range(n):
    a = int(input())
    if a>1 :
        pn.append(a)
    elif a==1:
        r+=1
    else:
        mn.append(a)

mn.sort()
pn.sort(reverse=True)
Q=deque()
for i in range(len(pn)):
    Q.append(pn[i])
while len(Q)>1:
    a = Q.popleft()
    b = Q.popleft()
    r+= a*b
if Q:
    r+=Q.popleft()

Q=deque()
for i in range(len(mn)):
    Q.append(mn[i])
while len(Q)>1:
    a = Q.popleft()
    b = Q.popleft()
    r+= a*b
if Q:
    r+=Q.popleft()

print(r)
