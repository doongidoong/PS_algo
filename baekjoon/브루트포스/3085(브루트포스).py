import sys

sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")

n= int(input())
l = list(list(sys.stdin.readline()) for _ in range(n))

def h_change(k,a,b):
    global answer
    temp=1
    for j in range(1,n):
        if l[k][j] == l[k][j-1]:
            temp+=1
        else:
            temp=1  
        if answer < temp:
            answer =temp
    
    for i in range(a,b+1):
        temp=1
        for j in range(1,n):
            if l[j][i] == l[j-1][i]:
                temp+=1
            else:
                temp=1
            
            if answer < temp:
                answer =temp    
    return answer
def v_change(k,a,b):
    global answer
    for i in range(a,b+1):
        temp=1
        for j in range(1,n):
            if l[i][j] == l[i][j-1]:
                temp+=1
            else:
                temp=1  
            if answer < temp:
                answer =temp
    temp=1
    for j in range(1,n):
        if l[j][k] == l[j-1][k]:
            temp+=1
        else:
            temp=1
        
        if answer < temp:
            answer =temp    
    return answer


answer=1
for i in range(n):
    for j in range(n):
        if i+1<n:
            l[i][j], l[i+1][j] = l[i+1][j], l[i][j]
            v_change(j,i,i+1)
            l[i][j], l[i+1][j] = l[i+1][j], l[i][j]
        if j+1<n:
            l[i][j], l[i][j+1] =  l[i][j+1], l[i][j]
            h_change(i,j,j+1)
            l[i][j],  l[i][j+1] =  l[i][j+1], l[i][j]
        


print(answer)