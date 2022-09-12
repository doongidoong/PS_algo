from this import d


boards =[]
def solution(m, n, board):
    global boards
    boards =board
    answer = 0
    return answer


def checkBlock(x,y):
    dx =[0,1,0,1]
    dy = [0,1,0,1]
    for i in range(4):
        xx = x+ dx[i]
        yy = y + dy[i]
        if boards[x][y]!=boards[xx][yy]:
             return False
    return True

def chagneBlock(x,y):
    dx =[0,1,0,1]
    dy = [0,1,0,1]
    for i in range(4):
        xx = x+ dx[i]
        yy = y + dy[i]
        boards[xx][yy] ='*'

def deleteBlcok():
    for i in range(len(boards)):
        for j in range(len(boards[i])):
            if boards[i][j] == '*':
                now = i
                while now > 0 :
                    temp = boards[now][j]
                    boards[now][j] = boards[now-1][j]
                    boards[now-1][j] = temp
                    now = now-1

