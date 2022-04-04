def solution(money):
    answer = 0
    dy1 = [0 for i in range(len(money))]
    dy2 = [0 for i in range(len(money))]
    if len(money)==3:
        return max(money)
    for i in range(0,len(money)-1):
        if i==0:
            dy1[0]=money[0]
        elif i==1:
            dy1[1]=money[1]
        elif i==2:
            dy1[2]=money[0]+money[2]
        else:
            dy1[i]= max(dy1[i-2],dy1[i-3])+money[i]
    for i in range(1,len(money)):
        if i==1:
            dy2[1]=money[1]
        elif i==2:
            dy2[2]=money[2]
        elif i==3:
            dy2[3]=money[1]+money[3]
        else:
            dy2[i]= max(dy2[i-2],dy2[i-3])+money[i]
    answer= max(max(dy1),max(dy2))
    return answer



money = [1,2,3,1,5]
print(solution(money))