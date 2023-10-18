from collections import defaultdict
def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    d1 = defaultdict(int)
    d2 = defaultdict(int)
    lStr1 = 0
    lStr2 = 0
    for i in range(len(str1)-1):
        a = str1[i]
        b = str1[i+1]
        if 65<= ord(a)<=90 and 65<= ord(b)<=90:  
            s= a+b
            d1[s] +=1
            lStr1 +=1
    for i in range(len(str2)-1):
        a = str2[i]
        b = str2[i+1]
        if 65<= ord(a)<=90 and 65<= ord(b)<=90:  
            s= a+b
            d2[s] +=1
            lStr2 +=1
    ans = 0
    for key, val in d1.items():
        ans += min(val,d2[key])
    if lStr1 + lStr2 == 0:
        return 65536
    answer = ans/(lStr1+lStr2-ans)
    return int(answer*65536)

print(solution("E=M*C^2", "e=m*c^2"))