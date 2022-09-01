from datetime import datetime, timedelta

lines = ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]

def solution(lines):
    L = []
    for line in lines:
        date, time , duration = line.split(' ')
        endTime = datetime.strptime(date+' '+time,'%Y-%m-%d %H:%M:%S.%f')
        duration = float(duration.replace('s',''))
        startTime = endTime - timedelta(seconds =duration-0.001)
        L.append((startTime,endTime))
    maxCnt = 0
    for i in range(len(L)):        
        normTime =  L[i][1]
        cnt=0
        for j in range(i,len(L)):
            startTime = L[j][0]
            if normTime > startTime- timedelta(seconds = 1):
                # print(L[i][0], L[i][1],startTime- timedelta(seconds = 1))
                cnt+=1
        if cnt>=maxCnt:
            maxCnt = cnt
    return maxCnt
# print(solution(lines))