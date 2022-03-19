
def solution(brown, yellow):
    answer = []
    tot = brown+yellow
    for i in range(3,brown//2+1):
        if tot%i==0:
            a = i
            b = tot//a
            if yellow%(a-2)==0 and yellow/(a-2) == b-2:
                answer.append(b)
                answer.append(a)
                break
                    
    return answer