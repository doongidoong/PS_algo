def solution(N, number):
    answer = -1
    dp = [[]for _ in range(9)]
    dp[0].append(0)
    dp[1].append(N)
    if number==N:
        return 1
    for i in range(2,9):
        temp=[]
        temp.append(int(str(N)*(i)))
        for j in range(1,i//2+1):
            for a in dp[j]:
                for b in dp[i-j]:
                    temp.append(a+b)
                    temp.append(a*b)
                    temp.append(a-b)
                    temp.append(b-a)
                    if a:
                        temp.append(b//a)
                    if b:
                        temp.append(a//b)
        dp[i] = list(set([x for x in temp if x>=1 and x<=32000]))
        if number in dp[i]:
            answer=i
            break
    return answer

N= 2
number = 11
solution(N,number)