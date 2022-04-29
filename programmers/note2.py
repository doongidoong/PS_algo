from collections import deque
def solution(bridge_length, weight, truck_weights):
  
    answer = 0
    L = [0]*bridge_length
    bridge = deque(L)
    temp = 0
    pos = 0
    while pos<len(truck_weights):
        answer+=1
        temp -= bridge.popleft()
        if temp+truck_weights[pos]<=weight:
            bridge.append(truck_weights[pos])
            temp+=truck_weights[pos]
            pos+=1
        else:
            bridge.append(0)
    answer += len(bridge)
    return answer

bridge_length = 2 
weight = 10
truck_weights =[7,4,5,6]

solution(bridge_length, weight, truck_weights)