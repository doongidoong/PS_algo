import heapq

def solution(operations):
    minh=[]
    maxh=[]
    answer = []
    cnt=0
    p = []

    for i in range(len(operations)):
        order, num = operations[i].split()
        num = int(num)
        if order=='I':
            heapq.heappush(minh,num)
            heapq.heappush(maxh,num*(-1))
        else:
            if num==-1 and minh:
                heapq.heappop(minh)
                if minh ==[] or minh[0]>-maxh[0]:
                    minh=[]
                    maxh=[]
            else:
                heapq.heappop(maxh)
                if maxh==[] or minh[0]>-maxh[0]:
                    minh=[]
                    maxh=[]
    if minh:
        b = -heapq.heappop(maxh)
        a= heapq.heappop(minh)       
        answer.append(b)
        answer.append(a)
    else:
        answer = [0,0]
    return answer

operations = ["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]
print(solution(operations))

