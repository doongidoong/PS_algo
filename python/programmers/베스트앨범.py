from collections import defaultdict
def solution(genres, plays):
    answer=[]
    d = defaultdict(int)
    d2 = defaultdict(list)
    for i in range(len(genres)):
        d[genres[i]]+=plays[i]
        d2[genres[i]].append((-1*plays[i],i))
    for t in range(len(d)):
        cnt=0
        maxv = 0
        for k,v in d.items():
            if v>maxv:
                maxv=v
                target=k
        tmp = d2[target]
        tmp.sort()
        for i in tmp[:2]:
            answer.append(i[1])
        d[target] = 0
    
    return answer