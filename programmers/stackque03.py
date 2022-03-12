from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque()
    for i in range(bridge_length):
        q.append(0)
    pos= 0
    temp= 0
    out =0
    while q:
        answer += 1
        t= q.popleft()
        if t==1:
            temp -=truck_weights[out]
            out +=1
        if pos < len(truck_weights):
            if temp + truck_weights[pos] <= weight:
                temp+=truck_weights[pos]
                pos+=1
                q.append(1)
            else:
                q.append(0)
    
    return answer
    
bridge_length=2	
weight = 10
truck_weight = [7,4,5,6]

print(solution(bridge_length, weight, truck_weight))