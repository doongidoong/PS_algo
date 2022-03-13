import heapq
def solution(scoville, K):
    answer = 0
    h = []
    for i in scoville:
        heapq.heappush(h,i)
    while h:
        a=heapq.heappop(h)
        if a>=k:
            return answer
        b=heapq.heappop(h)
        heapq.heappush(h,a+2*b)
        answer+=1
    else:
        return -1

sco= [1, 2, 3, 9, 10, 12]	
k = 7
print(solution(sco,k))
