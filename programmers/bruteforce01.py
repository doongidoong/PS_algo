def person1(ans):
    arr =[1,2,3,4,5]
    cnt=0
    for i in range(len(ans)):
        if arr[i%5] ==ans[i]:
            cnt+=1
    return cnt
def person2(ans):
    arr=[ 2, 1, 2, 3, 2, 4, 2, 5]
    cnt=0
    for i in range(len(ans)):
        if arr[i%8] ==ans[i]:
            cnt+=1
    return cnt
def person3(ans):
    arr=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt=0
    for i in range(len(ans)):
        if arr[i%10] ==ans[i]:
            cnt+=1
    return cnt
def solution(ans):
    answers=[]
    a = []
    a.append(person1(ans))
    a.append(person2(ans))
    a.append(person3(ans))
    for i in range(3):
        if max(a)==a[i]:
            answers.append(i+1)
    return answers

ans = [1,3,2,4,2]

print(solution(ans))