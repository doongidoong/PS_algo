course	 = [2,3,4]	
orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
answer  = []
d = {}

def solution(orders, course):
    answer = []
    for i in range(len(orders)):
        string = sorted(list(orders[i]))
        DFS(-1,'',string)
    courseHash = [0 for i in range(1,11)]
    courseAnswer = [ [] for i in range(1,11)]
    for i in course:
        courseHash[i] =1
    for a,b in d.items():
        if courseHash[len(a)] > 0: 
            if b>1 and b == courseHash[len(a)] :
                courseAnswer[len(a)].append(a)
            elif b > courseHash[len(a)] : 
                courseHash[len(a)] = b
                courseAnswer[len(a)] = [a]
    for i in courseAnswer:
        if i :
            for j in i:
                answer.append(j)
    answer.sort()
    print(answer)
    return answer

def DFS(L, str,order):
    if len(str)>=2:
        d[str] = d.get(str,0)+1
    for i in range(L+1, len(order)):
        DFS(i,str+order[i],order)

solution(orders,course)