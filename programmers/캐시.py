from traceback import print_tb


def solution(cacheSize, cities):
    answer = 0
    cash =[]
    for citie in cities:
        citie = citie.lower()
        if cash and citie in cash:
            cash.pop(cash.index(citie))
            answer +=1
        else:
            answer +=5
        if len(cash)<cacheSize :
            cash.append(citie)
        else:
            if cash:
                cash.pop(0)
                cash.append(citie)
    return answer

#print(solution(5,	["A", "B", "C", "B","D","E"]))