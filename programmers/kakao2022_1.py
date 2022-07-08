from collections import defaultdict
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k=2

d = defaultdict(set)

def solution(id_list, report, k):
    for i in range(len(report)):
        a, b =report[i].split()
        d[b].add(a)
    for i in range(len(id_list)):
        if len(d[id_list[i]]) >=k:
            for j in d[id_list[i]]:
                print(j)

    answer = []
    return answer

solution(id_list,report,k)
