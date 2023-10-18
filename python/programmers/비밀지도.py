
def solution(n, arr1, arr2):
    answer = []
    temp = []
    for i in range(n):
        temp.append(bin(arr1[i]|arr2[i]))
    print(temp)
    for i in temp:
        i= i.replace('0b','')        
        if len(i) < n :
            i = '0'*(n-len(i)) + i
        i= i.replace('0',' ')        
                
        i= i.replace('1','#')
        answer.append(i)    
    return answer


print(solution(6, [46, 33, 33 ,22, 31, 50], 	[27 ,56, 19, 14, 14, 10])   )