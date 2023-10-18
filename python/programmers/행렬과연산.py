from collections import deque

d = {}
def solution(rc, operations):
    answer = []
    ls = deque()
    rs = deque()
    lrc = len(rc)
    for i in range(lrc):
        temp = deque()
        for j in range(len(rc[0])):
            if j==0:
                ls.append(rc[i][j])
            elif j == len(rc[0]) -1:
                rs.append(rc[i][j])
            else:
                temp.append(rc[i][j])
        d[i] = temp
    d['ls'] = ls
    d['rs'] = rs
    start = 0 
    for i in range(len(operations)):
        if operations[i] == "ShiftRow":
            temp = d[lrc-1]
            start=(start+lrc-1)%lrc
            d['ls'].appendleft(d['ls'].pop())
            d['rs'].appendleft(d['rs'].pop())
        else:
            d[(start+lrc-1)%lrc].append(d['rs'].pop())
            d[start].appendleft(d['ls'].popleft())
            d['rs'].appendleft(d[start].pop())
            d['ls'].append(d[(start+lrc-1)%lrc].popleft())
    for i in range(lrc):
        temp = []
        for j in range(len(rc[0])):
            if j==0:
                temp.append(d['ls'][i])
            elif j == len(rc[0]) -1:
                temp.append(d['rs'][i])
            else:
                temp.append(d[(i+start)%lrc][j-1])
        answer.append(temp)
    return answer
