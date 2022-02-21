import sys
from collections import deque 
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

a,b = map(int,input().split())

Q= deque()
Q.append((b,1))
while Q:
    b,dis = Q.popleft()
    if b==a:
        print(dis)
        break
    if b%10 == 1:
        Q.append(((b-1)//10,dis+1))
    else:
        if b%2 ==1 or b<a:
            print(-1)
            break
        Q.append((b//2,dis+1))
else:
    print(-1)