import sys

sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")

def DFS(x,y):
    global cnt
    if x==6 and y==6:
        cnt+=1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<=6 and 0<=yy<=6 and board[xx][yy] ==0:
                board[xx][yy] =1
                DFS(xx,yy)
                board[xx][yy] = 0

        

board = [list(map(int, input().split())) for _ in range(7)]
dx =[1,-1,0,0]
dy =[0,0,1,-1]
cnt =0
board[0][0]=1
DFS(0,0)
print(cnt)

"""내풀이
d =list([0]*9 for _ in range(9))
d[1][1]=1
dx =[1,-1,0,0]
dy =[0,0,1,-1]
cnt=0
def dfs(x,y):
    global cnt
    if x==7 and y ==7:
        cnt+=1
        return
    else:
        for i in range(4):
            a = x+dx[i]
            b = y+dy[i]
            if L[a][b] ==0 and d[a][b] ==0:
                d[a][b] = 1
                dfs(a,b)
                d[a][b] = 0
                

L=[[1]*9]
for i in range(7):
    L.append([1]+list(map(int, input().split()))+[1])

L.append([1]*9)
dfs(1,1)
print(cnt)
"""