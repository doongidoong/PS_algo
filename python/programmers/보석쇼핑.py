
def solution(gems):
    d = {gems[0]:1}
    setGems = set(gems)
    gemKindLen = len(setGems)
    gemLen = len(gems)
    answer = [0,gemLen]
    lt = 0 
    rt = 0
    while rt<gemLen:
        if len(d) < gemKindLen :
            rt +=1
            if rt == gemLen:
                break
            d[gems[rt]] = d.get(gems[rt],0) +1
        else:
            if (rt-lt+1) < (answer[1]-answer[0]+1):
                answer = [lt+1,rt+1]
            if d[gems[lt]] == 1:
                del d[gems[lt]]
            else:
                d[gems[lt]] = d[gems[lt]] - 1 
            lt+=1
    return answer
