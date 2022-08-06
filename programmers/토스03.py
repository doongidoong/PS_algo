from collections import Counter

def solution(tasks):
    answer=0
    d = Counter(tasks)
    for a,cnt in d.items():
        if cnt ==1:
            return -1
        while cnt>=5:
            cnt-=3
            answer+=1
        if cnt==4:
            answer+=2
        else:
            answer+=1
    return answer


tasks = [1, 1, 2, 3, 3, 2, 2]

solution(tasks)