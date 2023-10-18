from collections import deque
def solution(progresses, speeds):
    p = deque(progresses)
    s = deque(speeds)
    time=0
    cnt = 0
    answer = []
    while p:
        rest=100 - time*s[0]-p[0]  
        if rest<=0:
            p.popleft()
            s.popleft()
            cnt+=1
        else:
            time += rest//s[0]
            if rest%s[0]>0:
                time+=1
            if cnt>0:
                answer.append(cnt)
                cnt=0
    answer.append(cnt)
    return answer                
genres=[93, 30, 55]	

plays=[1, 30, 5]
print(solution(genres,plays))
