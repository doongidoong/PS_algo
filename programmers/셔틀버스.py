def solution(n, t, m, timetable):
    answer = ''
    people =[]
    for i in timetable:
        hour, minute = i.split(':')
        people.append(int(hour)*60 +int(minute))
    people.sort()
    # print(people)
    busTime = 9*60
    busRemain = n
    while busRemain:
        # print(busTime)
        if busRemain == 1:
            if len(people) >= m and people[m-1]-1 < busTime:
                    answer = people[m-1]-1
            else:
                answer = busTime
        else:
            cnt = 0
            while len(people)>cnt and people[cnt]<= busTime:
                cnt+=1
                if cnt >= m:
                    break
            people = people[cnt:]
        busRemain -= 1
        busTime = busTime + t
    hour = "{:0>2}:".format(answer//60)
    minute = "{:0>2}".format(answer%60)
    answer = hour+minute
    return answer