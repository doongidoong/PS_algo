from collections import deque


def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    cnt = 0
    s1  = sum(queue1)
    s2  = sum(queue2)
    while cnt <  600000:
        if s1==0 or s2==0 :
            return -1
        if s1 == s2:
            return cnt
        elif s1 < s2 :
            pNum  = queue2.popleft()
            queue1.append(pNum)
            s1 += pNum
            s2 -= pNum
        elif s1 > s2 :
            pNum  = queue1.popleft()
            queue2.append(pNum)
            s2 += pNum
            s1 -= pNum        
        cnt+=1
    return -1

print(solution(	[1, 1, 1, 1, 1], [1, 1, 1, 9, 1]))