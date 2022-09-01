from datetime import datetime, timedelta

lines = [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]
def solution(lines):
    L = []

    for t in lines:
        time = t.split(" ")
        a= get_start_time(time[1], time[2])
        b= get_time(time[1])
        L.append((a,b))
    maxCnt = 0

    for i in range(len(L)):        
        normTime =  L[i][1]
        cnt=0
        for j in range(i,len(L)):
            if normTime >  L[j][0]- 1000:
                cnt+=1
        if cnt>=maxCnt:
            maxCnt = cnt
    return maxCnt

def get_time(time):
    hour = int(time[:2]) * 3600
    minute = int(time[3:5]) * 60
    second = int(time[6:8])
    millisecond = int(time[9:])
    return (hour + minute + second) * 1000 + millisecond


def get_start_time(time, duration_time):
    n_time = duration_time[:-1]
    int_duration_time = int(float(n_time) * 1000)
    return get_time(time) - int_duration_time + 1
print(solution(lines))