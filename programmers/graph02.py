
def solution(n, results):
    answer = 0
    player = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in results:
        player[i[1]][i[0]]= 1
        player[i[0]][i[1]]= -1
    for i in range(1,n+1):
        lost = []
        win = []
        for j in range(1,n+1):
            if player[i][j] == 1:
                lost.append(j)
            elif player[i][j] == -1:
                win.append(j)
        while lost:
            p = lost.pop()
            for k in range(1,n+1):
                if player[p][k] == 1 and player[i][k] == 0 :
                    player[i][k] = 1
                    lost.append(k)
        while win:
            p = win.pop()
            for k in range(1,n+1):
                if player[p][k] == -1 and player[i][k] == 0 :
                    player[i][k] = -1
                    win.append(k)
        if player[i].count(0) == 2:
            answer+=1
        
    return answer
n= 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

print(solution(n,results))