import sys
from collections import deque
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

board  =  ''.join([ input().replace(' ','') for _ in range(3)])
dx=[1,-1,3,-3]

visit = {}
Q = deque()
x = board.index('0')
visit[board] = 0
Q.append((board,x))
answer = '123456780'
while Q:
    check =0
    t = Q.popleft()
    p = t[0]
    cnt = visit[p]
    if p==answer:
        print(cnt)
        break
    i = t[1]
    for k in range(4):
        a= i+dx[k]
        if k<2 and a//3 != i//3:
            continue
        if 0<=a<=8 :
            temp =''
            for s in range(9):
                if s== i:
                    temp+=p[a]
                elif s== a:
                    temp+=p[i]
                else:
                    temp+=p[s]
            if visit.get(temp,-1) >=0:
                continue
            else:
                visit[temp] = cnt+1
                Q.append((temp,a))

else : 
    print(-1)