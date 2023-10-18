def Count(t, times):
    sumt = 0
    for i in times:
        sumt += t//i

    return sumt


def solution(n, times):
    answer = 1000000001
    lt =0
    rt = 1000000000*1000000000
    times.sort()
    while lt<=rt:
        mid = (lt+rt)//2
        c= Count(mid,times)
        if n <= c :
            answer=mid 
            rt = mid-1
        else:
            lt = mid+1
    return answer