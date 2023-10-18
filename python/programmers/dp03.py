def solution(m, n, puddles):
    dy=[[0 for _ in range(m)] for _ in range(n)]
    dy[0][0]=1
    for i in puddles:
        dy[i[1]-1][i[0]-1]=-1
    def DFS(y,x):
        if dy[y][x]==-1 or x<0 or y<0:
            return 0
        if dy[y][x]!=0:
            return dy[y][x]
        else:
            dy[y][x] = DFS(y-1,x)+DFS(y,x-1)
            return dy[y][x]
    DFS(n-1,m-1)
    return (dy[-1][-1]) % 1000000007




m= 4	
n= 3	


puddles = [[2, 2]]
solution(m,n,puddles)
