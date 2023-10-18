import sys
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\samsung\\input.txt","r")

n, m ,x ,y , k = map(int,input().split())

L = [ list(map(int, input().split())) for _ in range(n)]
command = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0]
#  2
#4 1 3
#  5
#  6
def turn(case, dice):
    a, b, c, d, e, f = dice[0] , dice[1], dice[2], dice[3], dice[4], dice[5]
    if case == 1: #오른쪽
        dice =[d,b,a,f,e,c]
    if case == 2: #왼쪽
        dice =[c,b,f,a,e,d]
    if case == 3: #위쪽
        dice =[b,f,c,d,a,e]
    if case == 4: #아래
        dice =[e,a,c,d,f,b]
    return dice

dx= [0, 0, 0,  -1, 1]
dy= [0, 1, -1, 0, 0]
#위는 dice[0] 아래는 dice[5]
start = [x,y]
for i in range(len(command)):
    xx = start[0] +dx[command[i]]
    yy = start[1] +dy[command[i]]
    if 0 <= xx <= n-1 and 0 <= yy <= m-1 :
        dice = turn(command[i], dice)
        if L[xx][yy] == 0:
            L[xx][yy] = dice[5]
        else:
            dice[5] = L[xx][yy]
            L[xx][yy] = 0
        start = [xx,yy]
        print(dice[0])

