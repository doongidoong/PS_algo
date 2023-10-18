def solution(n, lost, reserve):
    d=[1]*(n+1)
    for i in reserve:
        d[i]+=1
    for i in lost:
        d[i]-=1
    d[0]=0
    cnt=0
    lost.sort()
    for i in lost:
        if d[i]==1:
            continue
        if d[i-1]==2:
            d[i-1]=1
            continue
        if i+1<=n and d[i+1]==2:
            d[i+1]=1
            continue
        cnt+=1
    answer = n-cnt
    return answer