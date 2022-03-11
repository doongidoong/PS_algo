from collections import deque
def solution(bridge_length, weight, truck_weight):
    answer = 0
    pos =0
    bridge = deque()
    dis= dict()
    
bridge_length=2	
weight = 10
truck_weight = [7,4,5,6]

print(solution(bridge_length, weight, truck_weight))