import heapq
def solution(j):
    answer = 0
    h=[]
    t=0
    cnt=0
    jobs=[]
    for i in j:
        heapq.heappush(jobs,i)
    while cnt<len(j):
        while jobs and jobs[0][0]<=t:
            a= heapq.heappop(jobs)
            heapq.heappush(h,(a[1],a[0]))
        if h :
            now = heapq.heappop(h)
            t+=now[0]
            answer += t-now[1]
            cnt+=1
        else:
            t+=1
    answer = answer//len(j)
    return answer

jobs =[[0, 3], [1, 9], [2, 6]]
print(solution(jobs))