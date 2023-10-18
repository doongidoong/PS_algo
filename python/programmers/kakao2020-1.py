from collections import defaultdict
def solution(s):
    n = len(s)
    answer = n
    for i in range(n//2+1,0,-1):
        L = []
        for j in range(0,n,i):
            L.append(s[j:j+i])
        ans = ''
        now = L[0]
        cnt = 1
        for i in range(1,len(L)):
            if L[i-1] == L[i]:
                cnt+=1
            else:
                if cnt>1:
                    ans += L[i-1]+str(cnt)
                else:
                    ans += L[i-1]
                cnt=1
        if cnt>1:
            ans += L[-1]+str(cnt)
        else:
            ans+= L[-1]
        answer = min(len(ans),answer)
    
    return answer





s = "aabbaccc"
print(solution(s))
# "ababcdcdababcdcd"	
# "abcabcdede"	
# "abcabcabcabcdededededede"	
# "xababcdcdababcdcd"	