hash = {"zero":0, "one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8 ,"nine":9 }

def solution(s):
    temp=""
    answer=""
    for i in s:
        if 97<=ord(i) and ord(i)<=122:
            temp+=i
            if hash.get(temp,-1)!=-1:
                answer= answer+ str(hash[temp])
                temp=""
        else:
            answer+=i

        
    return int(answer)

solution("1zerotwozero3")