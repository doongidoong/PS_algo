from cmath import inf


def solution(m, n, puddles):
    DFS(n-1,m-1)
    answer = 0
    return answer
def DFS(x,y):
    if dy[x][y]!=0:
        return dy[x][y]
    else:
        if x == 0 and 0<=y<m:
            dy[x][y] = 1 + DFS(0,y-1)
        if y == 0 and 0<=x<n:
            dy[x][y] =1 + DFS(x-1,0)
        else:
            dy[x][y] = min(DFS(x-1,y),DFS(x,y-1))+1
        return dy[x][y] 
     
    DFS(x+1,y)
    DFS(x,y+1)
m= 4	
n= 3	
dy=[[0 for _ in range(m)] for _ in range(n)]
puddles = [[2, 2]]
solution(m,n,puddles)