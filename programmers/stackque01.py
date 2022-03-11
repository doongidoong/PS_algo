
def solution(progresses, speeds):
    stack= []
    time=0
    answer = []
    for i in range(len(progresses)):
        rest=100 - time*speeds[i]-progresses[i]  
        if rest>0:
            cnt=0
            while stack:
                stack.pop()
                cnt+=1
            if cnt>0:
                answer.append(cnt)
            stack.append(progresses[i])
            time += rest//speeds[i]
            if rest%speeds[i]>0:
                time+=1
        else:
            stack.append(progresses[i])
    answer.append(len(stack))
    
    return answer                
genres=[93, 30, 55]	

plays=[1, 30, 5]
print(solution(genres,plays))
