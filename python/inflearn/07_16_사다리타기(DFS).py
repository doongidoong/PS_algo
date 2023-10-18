import sys

#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")


def DFS(x, y):
    ch[x][y]=1
    if x==0:
        print(y)
    else:
        if y-1>=0 and board[x][y-1]==1 and ch[x][y-1]==0:
            DFS(x, y-1)
        elif y+1<10 and board[x][y+1]==1 and ch[x][y+1]==0:
            DFS(x, y+1)
        else:
            DFS(x-1, y)


board=[list(map(int, input().split())) for _ in range(10)]
ch=[[0]*10 for _ in range(10)]
for y in range(10):
    if board[9][y]==2: # 거꾸로 올라간다
        DFS(9, y)

"""내풀이
board = board=[list(map(int, input().split())) for _ in range(10)]

def dfs(L,x,y):
    ch[x][y]=1
    if board[x][y]==0:
        return
    if x==9:
        if board[x][y]==2:
            print(L)
        return  
    else:
        for i in (1,-1):
            if 0<= y+i <= 9:
                if board[x][y+i] == 1 and ch[x][y+i]==0:
                    dfs(L,x,y+i)
                    break
        else:
            dfs(L,x+1,y)            

for i in range(10):
    ch=[[0]*10 for _ in range(10)]
    dfs(i,0,i) 
    
"""