def solution(citations):
    citations.sort(reverse=True)
    cnt=0
    for i in range(len(citations)):
        if citations[i]<=cnt:
            break
        cnt +=1
    answer = cnt
    return answer
citations=[3, 0, 6, 1, 5]

print(solution(citations))