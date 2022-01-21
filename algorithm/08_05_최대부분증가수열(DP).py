import sys

sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")

n= int(input())
a = list(map(int,input().split()))
dy = [0]*(n)

dy[0] =1
res=0
for i in range(n):
    k=0
    md = 0
    while(k<i):
        if a[k]<a[i] and md<dy[k]:
            md=dy[k]
        k+=1
    dy[i] = md+1
    if res < dy[i]:
        res= dy[i]
print(res)


""" 
강의풀이

n=int(input())
arr=list(map(int, input().split()))
arr.insert(0,0)
dy=[0]*(n+1)
dy[1]=1
res=0
for i in range(2, n+1):
    max=0
    for j in range(i-1, 0, -1):
        if arr[j]<arr[i] and dy[j]>max:
            max=dy[j]
    dy[i]=max+1
    if dy[i]>res:
        res=dy[i]
print(res)

"""