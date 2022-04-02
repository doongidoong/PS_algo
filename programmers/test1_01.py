from collections import  defaultdict
def solution(n):
    k  = int(n**(0.5))+1
    answer = 0
    d=defaultdict(int)
    for i in range(1,k):
        if n%i ==0  :
            if d[i] !=1:
                answer+=i
                d[i]=1
            if d[n//i] !=1:
                answer+=n//i
                d[n//i]=1
    return answer

