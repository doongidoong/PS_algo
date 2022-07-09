lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]

def solution(lottos, win_nums):
    check = [0 for _ in range(46)]
    for i in range(len(win_nums)):
        check[win_nums[i]]=1
    cnt =0 
    undcnt = 0
    for i in lottos:
        if i==0:
            undcnt+=1
        else :
            if check[i] > 0 :
                cnt+=1
    rank = [6,6,5,4,3,2,1]
    answer = [rank[cnt+undcnt], rank[cnt]]
    return answer

print(solution(lottos,win_nums))