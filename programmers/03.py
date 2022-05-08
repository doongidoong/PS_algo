def solution(line):
    answer =[]
    keya = ["1","2","3","4","5","6","7","8","9","0"]
    keyb = ["Q","W","E","R","T","Y","U","I","O","P"]
    ls = "Q"
    rs = "P"
    lupper =0
    rupper =0
    for i in range(len(line)):
        upper=0
        if line[i] in keya:
            upper = 1
            loc = keya.index(line[i])
        else: 
            loc = keyb.index(line[i])
 
        if lupper == 1 :
            if upper :
                ld = abs(loc - keya.index(ls))
            else:
                ld = abs(loc - keya.index(ls))+1
        else:
            if upper :
                ld = abs(loc - keyb.index(ls))+1
            else:
                ld = abs(loc - keyb.index(ls))
        if rupper == 1 :
            if upper :
                rd = abs(loc - keya.index(rs))
            else:
                rd = abs(loc - keya.index(rs))+1
        else:
            if upper :
                rd = abs(loc - keyb.index(rs))+1
            else:
                rd = abs(loc - keyb.index(rs))
        if ld==rd:
            h1 = abs(lupper- upper)
            h2 = abs(rupper- upper)
            if h1==h2:
                if loc<=5:
                    answer.append(0)
                    lupper=upper
                    ls = line[i]
                else:
                    answer.append(1)
                rupper=upper
                rs = line[i]
            elif h1>h2:
                answer.append(0)
                lupper=upper
                ls = line[i]
            else:
                answer.append(1)
                rupper=upper
                rs = line[i]
        elif ld<rd:
            answer.append(0)
            lupper=upper
            ls = line[i]
        else:
            answer.append(1)
            rupper=upper
            rs = line[i]
    print(answer)
    return answer

line = "Q4OYPI"	

solution(line)