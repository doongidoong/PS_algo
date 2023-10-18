from collections import deque
import sys

sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\samsung\\input.txt","r")
board = [deque(map(int,input())) for _ in range(4)]
n = int(input())

#1 오른쪽 회전, -1 왼쪽회전


answer = 0
def turn(d,q):
    if d == -1:
        temp = q.popleft()
        q.append(temp)
    else:
        temp = q.pop()
        q.appendleft(temp)
    return q

for k in range(n):
    t, d = map(int, input().split())
    #오른쪽 체크
    tempTurn = [0,0,0,0]
    tempTurn[t-1]= d
    for i in range(t-1,3):
        if board[i][2] != board[i+1][6]:
            tempTurn[i+1] = tempTurn[i]*-1
        else:
            break
    for i in range(t-1,0,-1):
        if board[i][6] != board[i-1][2]:
            tempTurn[i-1] = tempTurn[i]*-1
        else:
            break
    for i in range(len(tempTurn)):
        if tempTurn[i] != 0:
            board[i] = turn(tempTurn[i],board[i])
answer = 0 
for i in range(4):
    if board[i][0]==1:
        answer += 2**(i)
print(answer) 