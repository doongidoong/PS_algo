from collections import defaultdict
def solution(rooms, target):
    answer = []
    name = []
    d = defaultdict(list)
    
    ope = defaultdict(int)
    for i in rooms:
        a , b = i.split(']')
        a= int(a[1:])
        L = list(b.split(','))
        for j in L:
            if j not in name:
                name.append(j)
            d[j].append(a)
   
    result =[ [] for i in range(len(name))]

    for i in range(len(result)):
        result[i].append(name[i])
    for key, val in d.items():
        if target in val:
            ope[key]=100000000
            continue
        ope[key]=len(val)
  
    for key, val in d.items():
        temp = 10000
        for j in val:
            temp = min(temp,abs(j-target))
        ope[key] +=ope[key]*5000+temp
    for i in range(len(result)):
        result[i].append(ope[result[i][0]])
    result.sort(key= lambda x: (x[1],x[0]))
 
    for j in range(len(result)):
        if result[j][1] >= 100000000:
            continue
        answer.append(result[j][0])
    return answer

rooms = ["[403]James", "[404]Azad,Louis,Andy", "[101]Azad,Guard"]	
target = 403



print(solution(rooms,target))