import sys
#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")
n = int(input())  
dx =[1,-1,0,0]
dy =[0,0,1,-1]

def DFS(x,y):
    global cnt
    cnt+=1
    board[x][y]=0
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<=n-1 and 0<=yy<=n-1 and board[xx][yy] == 1:
            DFS(xx,yy)

board = [list(map(int, input())) for _ in range(n)]
res = []
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            cnt =0
            DFS(i,j)
            res.append(cnt)
    
print(len(res))
res.sort()
for i in res:
    print(i)