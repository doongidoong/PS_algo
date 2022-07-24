check = []
answer =0
def solution(k, dungeons):
    global check, answer
    check = [0]*len(dungeons)
    DFS(0,dungeons,k)
    return answer


res = [0,0,0]
def DFS(level,dungeons,point):
    global answer
    answer = max(answer,level)
    
    for i in range(len(dungeons)):
        if check[i]==0 and point-dungeons[i][0]>=0:
            check[i]= 1
            DFS(level+1,dungeons,point-dungeons[i][1])
            check[i]=0

k= 80

dungeons = [[80,20],[50,40],[30,10]]	
print(solution(k,dungeons))