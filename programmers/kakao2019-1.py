def solution(record):
    answer = []
    action = []
    hash = {}
    for i in record:
        L = i.split()
        if L[0] == "Enter":
            hash[L[1]] = L[2]
            action.append([L[1],"님이 들어왔습니다."])
        elif L[0] == "Leave":
            action.append([L[1],"님이 나갔습니다."])
        elif L[0] == "Change":
            hash[L[1]] = L[2]
    for i in action:
        answer.append(hash[i[0]]+i[1])
    return answer