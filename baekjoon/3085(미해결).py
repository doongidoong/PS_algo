import sys

sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")

n= int(input())
l = list(list(input()) for _ in range(n))

def check(a,b):
    answer=1
    temp = 1
    for i in range(1,n):
        if l[i][b] == l[i-1][b]:
            temp+=1
        else :
            temp=1
        answer = max(answer,temp)
    temp = 1
    for j in range(1,n):
        if l[a][j] == l[a][j-1]:
            temp+=1
        else:
            temp=1
        answer = max(answer,temp)    
    return answer
answer=1
for i in range(n):
    for j in range(n):
        if i+1<n:
            answer = max(check(i,j),answer)
            l[i][j], l[i+1][j] = l[i+1][j], l[i][j]
            answer = max(check(i,j),answer)
            l[i][j], l[i+1][j] = l[i+1][j], l[i][j]
        if j+1<n:
            answer = max(check(i,j),answer)
            l[i][j], l[i][j+1] =  l[i][j+1], l[i][j]
            answer = max(check(i,j),answer)
            l[i][j],  l[i][j+1] =  l[i][j+1], l[i][j]
        


print(answer)