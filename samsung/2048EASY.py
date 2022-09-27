import copy

#위로부터 움직이는 함수, 위로 움직임
def MoveUp(board,n):
    flag = [[0]*n for _ in range(n)]
    g = copy.deepcopy(board)
    cnt = 1
    returnValue = 0
    while cnt > 0:
        cnt = 0
        for i in range(n):
            for j in range(n) :
                #0일 경우 pass
                if g[i][j] == 0:
                    continue
                returnValue = max(returnValue,g[i][j])
                #합쳐지는 것도 합치는 것도 합친 블럭이어서는 안된다.
                if i-1>=0 and flag[i][j] == 0  and flag[i-1][j] == 0 :
                    #같은 값일 경우 더함
                    if g[i-1][j] == g[i][j] :
                        g[i-1][j] += g[i][j]
                        flag[i-1][j] = 1
                        g[i][j] = 0
                        cnt +=1
                    #0일 경우, 옮기기만 함
                    elif g[i-1][j] == 0:
                        g[i-1][j] += g[i][j] 
                        g[i][j] = 0
                        cnt +=1
    return (g, returnValue) 


#아래로부터 움직이는 함수, 아래로 움직임
def MoveDown(board,n):
    flag = [[0]*n for _ in range(n)]
    g = copy.deepcopy(board)
    cnt = 1
    returnValue = 0
    while cnt > 0:
        cnt = 0
        #아래부터 시작해야하므로 반복문을 n-1부터 시작한다
        for i in range(n-1,-1,-1):
            for j in range(n) :
                if g[i][j] == 0:
                    continue
                returnValue = max(returnValue,g[i][j])
                if i+1<n and flag[i][j] == 0 and flag[i+1][j] == 0 :
                    if g[i+1][j] == g[i][j] :
                        g[i+1][j] += g[i][j]
                        flag[i+1][j] = 1
                        g[i][j] = 0
                        cnt +=1
                    elif g[i+1][j] == 0:
                        g[i+1][j] += g[i][j] 
                        g[i][j] = 0
                        cnt +=1
    return (g, returnValue) 

#왼쪽부터 움직이는 함수, 왼쪽으로 움직임
def MoveLeft(board,n):
    flag = [[0]*n for _ in range(n)]
    g = copy.deepcopy(board)
    cnt = 1
    returnValue = 0
    while cnt > 0:
        cnt = 0
        for i in range(n):
            for j in range(n) :
                if g[i][j] == 0:
                    continue
                returnValue = max(returnValue,g[i][j])
                if j-1>=0 and flag[i][j] == 0 and flag[i][j-1] == 0 :
                    if g[i][j-1] == g[i][j] :
                        g[i][j-1] += g[i][j]
                        flag[i][j-1] = 1
                        g[i][j] = 0
                        cnt +=1
                    elif g[i][j-1] == 0:
                        g[i][j-1] += g[i][j] 
                        g[i][j] = 0
                        cnt +=1
    return (g, returnValue) 


#오른쪽부터 움직이는 함수, 오른쪽으로 움직임
def MoveRight(board, n):
    flag = [[0]*n for _ in range(n)]
    g = copy.deepcopy(board)
    cnt = 1
    returnValue = 0
    while cnt > 0:
        cnt = 0
        for i in range(n):
            for j in range(n-1,-1,-1) :
                if g[i][j] == 0:
                    continue
                returnValue = max(returnValue,g[i][j])
                if j+1<n and flag[i][j] == 0 and flag[i][j+1] == 0 :
                    if g[i][j+1] == g[i][j] :
                        g[i][j+1] += g[i][j]
                        flag[i][j+1] = 1
                        g[i][j] = 0
                        cnt +=1
                    elif g[i][j+1] == 0:
                        g[i][j+1] += g[i][j] 
                        g[i][j] = 0
                        cnt +=1
    return (g, returnValue)

def DFS(L, board, n,ans):
    global answer
    if L == 5:
        answer = max(answer,ans)
        return
    #각 방향으로 탐색
    g1, maxNum = MoveUp(board,n)
    DFS(L+1, g1, n, maxNum)
    g2, maxNum = MoveDown(board,n)
    DFS(L+1, g2, n, maxNum)
    g3, maxNum = MoveLeft(board,n)
    DFS(L+1, g3, n, maxNum)
    g4, maxNum = MoveRight(board,n)
    DFS(L+1, g4, n, maxNum)


answer = 0  
n = int(input())
board = [ list(map(int,input().split())) for _ in range(n) ]
DFS(0,board,n,0)
print(answer)