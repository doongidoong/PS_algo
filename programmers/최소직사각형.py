def solution(sizes):
    minN=maxN=0
    for i in sizes:
        minN = max(minN,min(i[0], i[1]))
        maxN = max(maxN, max(i[0],i[1]))
    answer = maxN*minN
    return answer



sizes =[[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
print(solution(sizes))