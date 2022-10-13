def solution(registered_list, new_id):
    answer = new_id
    d = {}
    for i in registered_list:
        d[i] = 1
    #있는지 없는지 체크
    while True:
        if d.get(answer,0) == 0:
            return answer #없다면 Return
        #있다면 S와 N으로 분리한 뒤 N+1을 해준다
        s = ''
        n = ''
        for i in answer:
            if i.isdigit():
                n+=i
            else:
                s+=i
        if n =='':
            n= '0'
        intN = int(n)+1
        n = str(intN)
        answer = s+n


print(solution(
["cow1", "cow1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"], "cow"))