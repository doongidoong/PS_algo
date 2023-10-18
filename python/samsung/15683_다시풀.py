from itertools import permutations
import copy
import sys

sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\samsung\\input.txt","r")
n, m = map(int,input().split())
Realboard = [list(map(int,input().split())) for _ in range(n)]

mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]
# 북 - 동 - 남 - 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def fill(board, mm, x, y):
    for i in mm:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if board[nx][ny] == 6:
                break
            elif board[nx][ny] == 0:
                board[nx][ny] = 7

def right(i,j,board):
    for y in range(j,m):
        if board[i][y] == 6:
            break
        elif board[i][y] == 0:
            board[i][y] = '#'
    return board

def up(i,j,board):
    for x in range(i, -1,-1):
        if board[x][j] == 6:
            break
        elif board[x][j] == 0:
            board[x][j] = '#'
    return board

def down(i,j,board):
    for x in range(i, n):
        if board[x][j] == 6:
            break
        elif board[x][j] == 0:
            board[x][j] = '#'
    return board

def left(i,j,board):
    for y in range(j,-1,-1):
        if board[i][y] == 6:
            break
        elif board[i][y] == 0:
            board[i][y] = '#'
    return board
answer = 10000
cctv = []
for i in range(n):
    for j in range(m):
        if 1<=Realboard[i][j]<= 5 :
            cctv.append((Realboard[i][j], i,j))

def dfs(depth, arr):
    global min_value

    if depth == len(cctv):
        count = 0
        for i in range(n):
            count += arr[i].count(0)
        min_value = min(min_value, count)
        return
    temp = copy.deepcopy(arr)
    cctv_num, x, y = cctv[depth]
    for i in mode[cctv_num]:
        dfs(depth+1, temp)
        temp = copy.deepcopy(arr)

length = len(cctv)
print(length)
checkArr = [0]*length

print(answer)