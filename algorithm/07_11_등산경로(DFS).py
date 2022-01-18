import sys


def DFS(x,y):
    global cnt
    if x==end[0] and y==end[1]:
        cnt+=1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<=n-1 and 0<=yy<=n-1 and board[xx][yy] >board[x][y]:
                ch[xx][yy] =1
                DFS(xx,yy)
                ch[xx][yy] = 0
#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")
n = int(input())      
minn = 121321313
maxn = -121321313
board =[]
ch = [[0]*n for  _ in range(n)]

for  i in range(n):
    k = list(list(map(int, input().split())))
    board.append(k)
    a = min(k)
    b= max(k)
    if a < minn :
        minn =a
        start = (i,k.index(a))
    if b > maxn :
        maxn =b
        end = (i,k.index(b))
dx =[1,-1,0,0]
dy =[0,0,1,-1]
cnt =0
ch[0][0]=1
DFS(start[0],start[1])
print(cnt)