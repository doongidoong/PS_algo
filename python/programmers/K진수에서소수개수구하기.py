def solution(n, k):
    answer = 0
    sList = []
    s = ''
    if n == 0:
        s ='0'
    else:
        while n>0:
            mod = n%k 
            if mod != 0 :
                s= str(mod) + s
            else:
                if s and int(s) != 0:
                    sList.append(int(s))
                    s=''
            n = n//k
    sList.append(int(s))
    # dp = [1 for _ in range(maxNum+1) ] 
    # # print(dp)
    # dp[0] = 0
    # dp[1] = 0
    # for i in range(2,int(int(maxNum)**(0.5))+1):
    #     for j in range(2*i, int(maxNum)+1, i):
    #         dp[j] = 0
    for i in sList:
        if check(i):
            answer+=1
    return answer

def check(num):
    if num == 0 or num == 1:
        return False
    else:
        for i in range(2,int(num**0.5)+1):
            if num% i== 0:
                return False
        return True
        

