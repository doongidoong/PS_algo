check =[0]*200
answer=0
def solution(n, computers):
    global answer
    for i in range(n):
        if check[i]==0:
            check[i]=1
            DFS(i,computers)
            answer+=1
    return answer
def DFS(L,computers):
    if L==len(computers):
        return
    for i in range(0,len(computers)):

        if check[i]== 0 and computers[L][i]==1:
            check[i]=1
            DFS(i,computers)



n=3
computers= [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n,computers))