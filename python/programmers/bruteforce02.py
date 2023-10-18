from itertools import permutations

prime = [0]*(10000000)
def solution(numbers):
    prime[0]=1
    prime[1]=1
    for i in range(2,4000):
        for j in range(2*i,10000000,i):
            prime[j]=1
    s = list(numbers)
    cnt=0
    for i in range(1,len(s)+1):
        for j in list(permutations(s, i)):
            if prime[int(''.join(j))]==0:
                prime[int(''.join(j))]=1
                cnt+=1
    return cnt
numbers="011"
print(solution(numbers))