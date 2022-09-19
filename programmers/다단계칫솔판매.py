d = {}
s = {}
o = {}
def solution(enroll, referral, seller, amount):
    answer = []
    for i in range(len(enroll)):
        d[enroll[i]] = referral[i]
    for i in range(len(seller)):
        s={}
        findParent(s,seller[i], amount[i]*100)
        for person, money in s.items():
            o[person] = o.get(person,0) + money
    for i in range(len(enroll)):
        answer.append(o.get(enroll[i],0))
    print(answer)
    return answer


def findParent(s,x,money):
    if d[x]=='-' :
        toGive = int(money *0.1)
        if toGive >= 1 : 
            s['minsu'] = toGive
            s[x] = money - toGive            
            return
        else:
            s[x] = money
            return
    else:
        toGive = int(money *0.1)
        if toGive >= 1 : 
            s[x] = money - toGive
            findParent(s,d[x],toGive)
        else:
            s[x] = money




solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
    ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
    ["young", "john", "tod", "emily", "mary"],
    [12, 4, 2, 5, 10]	
    )