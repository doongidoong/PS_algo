from collections import defaultdict
import math
d = defaultdict(int)
d2 = {}
def solution(fees, records):
    answer =[]
    temp = []
    for record in records:
        time, num, com = record.split()
        t = int(time[0:2])*60 + int(time[3:5])
        d2[num] = com
        if com == 'IN':
            d[num] -= t
        else:
            d[num] += t
    for key, val in d2.items():
        if val == 'IN':
            d[key] += 23* 60 + 59
        
        if (d[key] - fees[0])/fees[2] == 0 or (d[key] - fees[0])/fees[2] < 0 :
            tf = 0
        else:
            tf = math.ceil((d[key] - fees[0])/fees[2])
        tf = int(tf)
        price = tf*fees[3] + fees[1]
        temp.append((key, price))
    temp.sort()
    for a, b in temp:
        answer.append(b)
    return answer

solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])