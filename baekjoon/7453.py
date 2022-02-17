import sys

sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n = int(input())
A=[]
B=[]
C=[]
D=[]
for i in range(n):
    a,b,c,d = map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
left=[]
for i in A:
    for j in B:
        left.append(i+j) 
right=[]
for i in C:
    for j in D:
        right.append(i+j) 
left.sort()
right.sort(reverse=True)

lt = 0
rt = 0
ans = 0
while lt < len(left) and rt < len(left):
    now = left[lt]+right[rt]
    if now == 0 :
        i= 1
        while lt+i < len(left) and left[lt] == left[lt+i]:
            i+=1
        j= 1
        while rt+j < len(right) and right[rt] == right[rt+j]:
            j+=1
        ans += i*j
        
        lt = lt+i
        rt = rt+j
    else:
        if now>0:
            rt+=1
        else:
            lt+=1
print(ans)

