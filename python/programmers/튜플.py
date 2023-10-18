from collections import defaultdict
from email.policy import default


d = defaultdict(int)
def solution(s):
    answer = []
    s = s[1:len(s)-1]
    cur = 0
    maxlen = 0
    while cur<len(s):
        if s[cur]=='{':
            cur+=1
            temp=''
            while True:
                if s[cur]=='}':
                    break
                else:
                    temp += s[cur]
                    cur+=1 
            templist = temp.split(',')
            for i in templist:
                if len(templist)>maxlen:
                    maxlen = len(templist)
                if d[i] ==0:
                    d[i] = len(templist)
                else:
                    d[i] = min(d[i], len(templist))
        cur+=1
    answer = [0 for i in range(maxlen)]
    for i in d.keys():
        answer[d[i]-1] =int(i)
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))