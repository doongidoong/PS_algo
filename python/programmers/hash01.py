from collections import Counter

def solution(participant, completion):
    d1 = Counter(participant)
    d2 = Counter(completion)
    for key,val in d1.items() :
        if d2[key] != val:
            return key
par = ["leo", "kiki", "eden"]
com = 	["eden", "kiki"]

print(solution(par,com))