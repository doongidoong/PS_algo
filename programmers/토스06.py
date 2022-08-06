from collections import defaultdict
def solution(invitationPairs):
    inv = defaultdict(int)
    invPerson = defaultdict(int)
    lastInv = defaultdict(int)
    
    tot = defaultdict(int)
    answer = []
    for i in range(len(invitationPairs)):
        a= invitationPairs[i][0]
        b= invitationPairs[i][1]
        invPerson[a]+=1
        inv[b]=a
        lastInv[a]=i
    for key,val in inv.items():
        tot[val]+=invPerson[key]
        if inv[val]:
            tot[inv[val]]+=invPerson[key] 
        # tot[key]+= 10*invPerson[key]
    print(inv)
    print(lastInv)
    print(invPerson)
    print(tot)
    return answer


invitationPairs=[[1, 2], [2, 3], [2, 4], [2, 5], [5, 6], [5, 7], [6, 8], [2, 9]]
solution(invitationPairs)
