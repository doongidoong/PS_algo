def solution(prices):
    answer=[0]*(len(prices))
    ind = 0
    for i in range(len(prices)-1,-1,-1):
        cnt = 0
        for j in range(i+1,len(prices)):
            cnt+=1
            if prices[i]>prices[j]:
                break
        answer[i] = min(cnt,len(prices)-i-1)
    return answer

prices = [1, 2, 3, 2, 3]
#[4, 3, 1, 1, 0]
print(solution(prices))