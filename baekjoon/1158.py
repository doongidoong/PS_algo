
import sys
from collections import deque 
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

n, k = map(int, input().split())
Q =deque()
for i in range(1,n+1):
    Q.append(i)
res =[]
cur =1
while Q:
    tmp =Q.popleft()
    if cur==k:
        res.append(tmp)
        cur=1
    else:
        Q.append(tmp)
        cur+=1
print('<', end='')
for i in range(len(res)):
    if i == len(res)-1:
        print(res[i],end='')
        break
    print(res[i], end=', ')

print('>')