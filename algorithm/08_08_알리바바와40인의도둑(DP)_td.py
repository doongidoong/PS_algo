import sys

#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")


def DFS(x,y):
    if dy[x][y]!=0:
        return dy[x][y]
    else:
        if x == 0 :
            dy[x][y] = a[0][y] + DFS(0,y-1)
        if y == 0:
            dy[x][y] =a[x][0] + DFS(x-1,0)
        else:
            dy[x][y] = min(DFS(x-1,y),DFS(x,y-1))+a[x][y]
        return dy[x][y] 


n= int(input())
a = [ list(map(int,input().split())) for _ in range(n)]

dy=[[0]*n for _ in range(n)]
dy[0][0] =a[0][0]

print(DFS(n-1,n-1))