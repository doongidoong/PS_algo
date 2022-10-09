from collections import defaultdict
maxNum = 10**8

numCombi = []
check = defaultdict(int)
def solution(numbers):
    answer =0
    for i in range(1,len(numbers)):
        DFS(numbers,0,i,0)
    return answer

def DFS(numbers,num, maxDepth,depth =0):
    if depth >= maxDepth:
        numCombi.append(num)
        return
    else:
        for i in range(len(numbers)):
            if check[numbers[i]]== 0:
                check[numbers[i]]= 1
                newNum = num*10+int(numbers[i])
                if CheckPrime(newNum):
                    DFS(numbers,newNum, maxDepth,depth =0)
                check[numbers[i]]= 0
def CheckPrime(num):
    for i in range(2, int(num**0.5)+1):
        if num% i ==0 :
            if i != num:
                return False
    return True

