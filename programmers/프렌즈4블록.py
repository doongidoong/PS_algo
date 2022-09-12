boards =[]
def solution(m, n, board):
    global boards
    for i in board:
        temp = []
        for j in i:
            temp.append(j)
        boards.append(temp)
    answer = 0

    while True:
        L = []
        for i in range(m-1):
            for j in range(n-1):
                if checkBlock(i,j):
                    L.append((i,j))
        if len(L) == 0:
            break
        for x,y in L:
            chagneBlock(x,y) 
        deleteBlock()
        # print(boards)
    for i in range(m):
        for j in range(n):
            if boards[i][j] =='*':
                answer+=1
    # print(answer)
    return answer


def checkBlock(x,y):
    dx =[0,1,0,1]
    dy = [0,0,1,1]
    if boards[x][y] =='*':
        return False
    for i in range(4):
        xx = x+ dx[i]
        yy = y + dy[i]
        if boards[x][y]!=boards[xx][yy] :
             return False
    return True

def chagneBlock(x,y):
    dx =[0,1,0,1]
    dy = [0,0,1,1]
    for i in range(4):
        xx = x+ dx[i]
        yy = y + dy[i]
        boards[xx][yy] ='*'

def deleteBlock():
    for i in range(len(boards)):
        for j in range(len(boards[i])):
            if boards[i][j] == '*':
                now = i
                while now > 0 :
                    temp = boards[now][j]
                    boards[now][j] = boards[now-1][j]
                    boards[now-1][j] = temp
                    now = now-1


solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])