def solution(stones, k):
    answer = 200000001
    lt = min(stones)
    rt = max(stones)
    while lt<=rt:
        mid = (lt+rt)//2
        people = 0
        for i in stones :
            cnt = i - mid
            if cnt <= 0:
                people += 1
            else:
                people = 0
            if people >= k:
                answer = min(answer,mid)
                rt = mid-1
                break
        else:
            lt = mid+1
    return answer
