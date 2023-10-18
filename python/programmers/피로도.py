answer = 0
def solution(k, dungeons):
    global checked
    checked= [0]*len(dungeons)
    DFS(k,dungeons,0)
    return answer

def DFS(point,dungeons,cnt):
    global answer
    for i in range(len(dungeons)):
        if checked[i]==0 and point >=dungeons[i][0]:
            checked[i]=1
            DFS(point-dungeons[i][1],dungeons,cnt+1)
            checked[i]=0
    answer = max(answer,cnt)
k= 80

dungeons = [[80,20],[50,40],[30,10]]	
print(solution(k,dungeons))