from collections import defaultdict
d = defaultdict(int)

def solution(k, room_number):
    answer = []
    for num in room_number:
        answer.append(find(num))


def find(num):
    if d[num] == 0 :
        d[num] = num + 1
        return num+1
    newNum = find(d[num])
    d[num] = newNum
    return newNum 

solution(10,[1,3,4,1,3,1])