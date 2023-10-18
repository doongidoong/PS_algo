import sys
from collections import deque

#가르키는 방향으로 움직인다.
def move(direct,now):
    x = now[0]
    y = now[1]
    if direct == 'R':
        return [x,y+1]
    if direct == 'L':
        return [x,y-1]
    if direct == 'D':
        return [x+1,y]
    if direct == 'U':
        return [x-1,y]

def chageDirect(now, com):
    if now == 'D': #아래를 향할 때
        if com == 'D': #오른쪽이라면 왼쪽이 된다.
            return 'L'
        else:
            return 'R'
    if now == 'U':
        if com == 'D': 
            return 'R'
        else:
            return 'L'
    if now == 'R':
        if com == 'D': 
            return 'D'
        else:
            return 'U'
    if now == 'L':
        if com == 'D': 
            return 'U'
        else:
            return 'D'


n = int(input())
k = int(input())
apples = [ list(map(int,input().split())) for i in range(k)]

L = int(input())
com = deque()
for i in range(L):
    time, direct = input().split()
    com.append([int(time),direct])
time = 0
snake = deque()
snake.append([1,1])
direct = 'R'

while True:
	#현재 뱀의 머리
    now = snake[0]
    
  	#머리를 돌려야하는지 판단
    if com and time == com[0][0] :
        direct = chageDirect(direct, com[0][1])
        com.popleft()
        
    #새로 이동할 뱀의 머리
    new = move(direct ,now)
    if 1 <= new[0] <= n and 1 <= new[1] <= n :
        flag = False
        #새로 이동할 머리가 뱀에 닿는가
        for i in snake:
            if i == new:
                flag = True
        time+=1
        if flag == True:
            break
        #새로 이동할 머리에 사과가 있는가
        if new not in apples :
            last = snake.pop()
        else:
            apples.remove(new)
        snake.appendleft(new)
    else:
        time+=1
        break  
print(time)