
def solution(atmos):
    answer = -1
    cnt =0
    maskon = 0
    abad= 81
    avbad = 151
    bbad= 36
    bvbad = 76  
    for i in range(len(atmos)):
        if maskon == 3:
            maskon=0
        if maskon==0 and (atmos[i][0]>=abad or atmos[i][1]>=bbad):
            cnt+=1
            maskon+=1
        elif maskon :
            maskon+=1
        
        if atmos[i][0]>=avbad and atmos[i][1]>=bvbad:
            maskon=3

    answer =cnt
    return answer


atmos = [[140, 90], [177, 75], [95, 45], [71, 31], [150, 30], [80, 35], [72, 33], [166, 81], [151, 75]]
print(solution(atmos))