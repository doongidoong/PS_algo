import sys

sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\samsung\\input.txt","r")
n, L = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]
answer = 0

for i in range(n):
    dp =[1]*n
    flag = 0
    for j in range(1,n):
        if board[j][i] == board[j-1][i] :
            dp[j] = dp[j-1]+1
        else:
            if abs(board[j][i] - board[j-1][i])>1:
                flag = 1
                break
            elif board[j][i] > board[j-1][i] :
                if dp[j-1] < L:
                    flag = 1 
                    break
            elif board[j][i] < board[j-1][i] :
                if dp[j-1] < 0:
                    flag =1
                    break
                dp[j] = -L+1
    if dp[-1]<0:
        flag = 1
    if flag == 0:
        answer +=1

for i in range(n):
    dp =[1]*n
    flag = 0
    for j in range(1,n):
        if board[i][j] == board[i][j-1] :
            dp[j] = dp[j-1]+1
        else:
            if abs(board[i][j] - board[i][j-1])>1:
                flag = 1
                break
            elif board[i][j] > board[i][j-1] :
                if dp[j-1] < L:
                    flag = 1 
                    break
            elif board[i][j] < board[i][j-1] :
                if dp[j-1] < 0:
                    flag =1
                    break
                dp[j] = -L+1
    if dp[-1]<0:
        flag = 1
    if flag == 0:
        answer +=1
print(answer)