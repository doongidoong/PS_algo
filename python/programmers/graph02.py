
def solution(n, results):
    answer = 0
    player = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in results:
        player[i[1]][i[0]]= 1
        player[i[0]][i[1]]= -1
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if player[i][k] == 1 and player[k][j] == 1:
                    player[i][j]=1
                if player[i][k] == -1 and player[k][j] == -1:
                    player[i][j]=-1
    for i in range(1,n+1):
        if player[i].count(0)==2:
            answer+=1
    return answer
n= 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

print(solution(n,results))