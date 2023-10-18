
def solution(m, n, puddles):
    dy=[[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i ==1 and j==1 :
                dy[1][1]=1
                continue
            if [j,i] in puddles:
                continue
            dy[i][j] = dy[i][j-1]+dy[i-1][j]
                
    return (dy[-1][-1]) % 1000000007

m= 4	
n= 3	


puddles = [[2, 2]]
solution(m,n,puddles)
