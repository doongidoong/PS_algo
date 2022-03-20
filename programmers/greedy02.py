# A 65 Z 
def move(next):
    return min(ord(next)-ord('A'),ord('Z')-ord(next)+1)
def findNext(name,now):
    lt=now
    rt=now
    cnt=0
    while cnt<len(name):
        cnt+=1
        lt-=1
        if lt==-1:
            lt=len(name)-1
        rt+=1
        if rt ==len(name):
            rt=0
        if name[lt]!='A' and name[rt]!='A':
            a,b = findNext(name,lt)
            c,d = findNext(name,rt)
            if a>c:
                return cnt,rt
            else:
                return cnt,lt
        elif name[lt]!='A':
            return cnt, lt
        elif name[rt]!='A':
            return cnt,rt
    return cnt,now

# AABAAABBBA
def solution(name):
    answer = 0
    now= 0
    name= list(name)
    if name[0]!='A':
        answer +=move(name[0])
        name[0]='A'
    while 1:
        cnt,next = findNext(name,now)
        print(cnt,now,next)
        if cnt==len(name):
            break
        answer+=cnt
        answer+=move(name[next])
        name[next]='A'
        now=next
    return answer

name = "BBBBBB"	
print(solution(name))