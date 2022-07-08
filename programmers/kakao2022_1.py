from collections import defaultdict
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k=2

def solution(id_list, report, k):
    d = defaultdict(set)
    index = {}
    id_len = len(id_list)
    answer = [0 for _ in range(id_len)]
    reports = [[0 for _ in range(id_len)] for _ in range(id_len)]
    for i in range(id_len):
        index[id_list[i]] = i
    for i in report:
        a,b = i.split()
        reports[index[b]][index[a]] =1
    for i in range(id_len):
        if sum(reports[i])>=k:
            for j in range(id_len):
                if reports[i][j]:
                    answer[j]+=1
    return answer
print(solution(id_list,report,k))
