from itertools import combinations
import sys


def check(board):
    for i in range(n):
        loc = i
        for j in range(h):
            if board[loc][j] != 0:
                loc+= board[loc][j]
        if i != loc:
            return False
    return True


sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\samsung\\input.txt","r")
n,m,h = map(int, input().split())
combi = [i for i in range((n-1)*h)]
board = [[0]*h for _ in range(n)]
for i in range(m):
    a, b = map(int,input().split())
    num = h*(b-1)+(a-1)
    board[b-1][a-1]  = 1
    board[b][a-1]  = -1

if check(board):
    print(0)

else:
    for k in range(1,4):
        for i in combinations(combi,k):
            numbers = list(i)
            flag = 0
            prevNum = -1
            for num in numbers:
                if num+h in numbers:
                    flag=1
                    break
            for num in numbers:
                a = num%h +1
                b = num//h +1
                if board[b-1][a-1]  != 0 or board[b][a-1]  != 0:
                    flag =1 
                    break
            if flag == 1:
                continue
            for num in numbers:
                a = num%h +1
                b = num//h +1
                board[b-1][a-1]  = 1
                board[b][a-1]  = -1 
            if check(board):
                print(k)
                sys.exit(0)
            for num in numbers:
                a = num%h +1
                b = num//h +1
                board[b-1][a-1]  = 0
                board[b][a-1]  = 0
    print(-1)  
#9, 17 ,21