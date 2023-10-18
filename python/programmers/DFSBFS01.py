answer= 0
def solution(numbers, target):
    answer=0
    DFS(0,0,len(numbers),target,numbers)
    return answer

def DFS(L,num,n,target,numbers):
    global answer

    if L==n:
        if num==target:
            answer+=1
        return 
    DFS(L+1,num-numbers[L],n,target,numbers)
    DFS(L+1,num+numbers[L],n,target,numbers)



numbers = [4, 1, 2, 1]
target=	4	
print(solution(numbers,target))