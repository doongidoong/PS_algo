from collections import deque
def solution(priorities, location):
    answer = 0
    Q = deque()
    for i in range(len(priorities)):
        Q.append(i)
    while Q:
        loc = Q.popleft()
        if max(priorities)==priorities[loc]:
            answer+=1
            if loc == location:
                return answer
            priorities[loc] =0
            continue
        else:
            Q.append(loc)
    return answer
