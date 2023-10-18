
import sys
from collections import deque

#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")

MAX = 10000

ch = [0] * (MAX+1)

dis = [0] * (MAX+1) #좌표를 인덱스로 사용함
 
n, m = map(int,input().split())

ch[n] = 1
dis[n] = 0  #처음 시작은 0번의 점프이므로 시작점 n 인덱스는 0부터 시작
dQ = deque()
dQ.append(n)

while dQ:
    now = dQ.popleft()
    if now==m:
        break
    for next in (now-1 ,now+1, now+5):
        if 0<next<=MAX :
            if ch[next] ==0:
                dQ.append(next)
                ch[next] =1
                dis[next] = dis[now] +1 #이전 행동에다가 1을 더한 것

print(dis[m])
