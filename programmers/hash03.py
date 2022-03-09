from collections import defaultdict
def solution(clohtes):
    d = defaultdict(int)
    for a,b in clohtes:
        d[b]+=1
    answer = 1
    for val in d.values():
        answer*=(val+1)

    return answer-1
                
#clohtes= [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
