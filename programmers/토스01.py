
def solution(s):
    answer =0
    L= [ 0 for _ in range(10)]
    now=1
    flag=0
    for i in range(1,len(s)):
        k=s[i]
        if s[i] ==s[i-1]:
            now+=1
            if now==3:
                L[int(k)]=int(k)
                now=1
                flag =1 
        else: 
            now= 1
    if flag== 0:
        answer = -1
    else:
        answer= int(str(max(L))*3)
    return answer


s= "111999333"
print(solution(s))