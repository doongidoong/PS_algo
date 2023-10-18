import sys
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\samsung\\input.txt","r")

n,m  = map(int, input().split())
x,y,d  = map(int, input().split())
board = [ list(map(int,input().split())) for _ in range(n)]
directTranspose = {0: 0, 1:3, 2:2, 3:1}
#d가 0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽

d = directTranspose[d]
direct = {0:[-1,0], 1:[0,-1], 2:[1,0], 3:[0,1]}

answer = 0

def turn(d,x,y):
    moveX, moveY = direct[(d+1)%4]
    if 0<=x+moveX <n and 0<=y+moveY <m and board[x+moveX][y+moveY] == 0:
        return True
    else:
        return False

while True:
    if board[x][y] == 0:
        answer +=1
        board[x][y] = -1
    startD = d
    while 1:
        if turn(d,x,y) :
            d = (d+1)%4
            moveX, moveY = direct[d]
            x = x+moveX
            y = y+moveY
            break
        else:
            d = (d+1)%4
            if d == startD:
                moveX, moveY = direct[d]
                if x-moveX<0 or y-moveY<0 or x-moveX>=n or y-moveY>=m or board[x-moveX][y-moveY] == 1:
                    print(answer)
                    sys.exit(0)
                x = x-moveX
                y = y-moveY
                