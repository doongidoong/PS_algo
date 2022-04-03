def solution(m, n, puddles):
    dy=[[0 for _ in range(m)] for _ in range(n)]
    dy[0][0]=1
    for i in puddles:
        dy[i[1]-1][i[0]-1]=-1
    DFS(n-1,m-1,dy)
    print(dy)
    return (dy[-1][-1]-2) % 1000000007
def DFS(y,x,dy):
    print(y,x)
    if dy[y][x]==-1 or x<0 or y<0:
        return 0
    if dy[y][x]!=0:
        return dy[y][x]
    else:
        dy[y][x] = DFS(y-1,x,dy)+DFS(y,x-1,dy)
        return dy[y][x]


m= 4	
n= 3	


puddles = [[2, 2]]
solution(m,n,puddles)
