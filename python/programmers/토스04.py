from collections import defaultdict

def solution(steps_one, names_one, steps_two, names_two, steps_three, names_three):
    answer=-1
    d1 = defaultdict(int)
    d2 = defaultdict(int)
    d3 = defaultdict(int)
    r =   defaultdict(int)
    s = set()
    for i in range(len(steps_one)):
        d1[names_one[i]] = max(d1[names_one[i]],steps_one[i])
        s.add(names_one[i])
    for i in range(len(steps_two)):
        d2[names_two[i]] = max(d2[names_two[i]],steps_two[i])
        s.add(names_two[i])

    for i in range(len(steps_three)):
        d3[names_three[i]] = max(d3[names_three[i]],steps_three[i])
        s.add(names_three[i])
    r = []
    for i in s:
        n = d1[i]+d2[i]+d3[i]
        r.append((d1[i]+d2[i]+d3[i],i))
    r.sort(key = lambda x : (x[0]*(-1),x[1]))
    print(r)
    answer = []
    for a,b in r:
        answer.append(b)
    return answer


steps_one=    [0, 5, 1]
names_one= ["evan", "ed", "evan"]
steps_two=  [9999]
names_two=  ["rose"]
steps_three=  [ 1]
names_three=  ["richard"]

# steps_one=    [1, 2, 3]
# names_one= ["james", "bob", "alice"]
# steps_two=  [10, 20, 30]
# names_two= ["james", "alice", "bob"]
# steps_three=  [1000, 1, 1]
# names_three= ["bob", "alice", "james"]

solution(steps_one, names_one, steps_two, names_two, steps_three, names_three)