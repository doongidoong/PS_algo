import sys

#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")

n= int(input())
a = [ list(map(int,input().split())) for _ in range(n)]
a.sort(reverse=True)
dy = [0]*(n)
dy[0] = a[0][1]
res=0
t =[]


for i in range(1,n):
    k=0
    maxh=0
    while(k<i):
        if a[k][0] > a[i][0] and a[k][2] > a[i][2] and maxh<dy[k]:
            maxh=dy[k]
        k+=1
    dy[i] = maxh + a[i][1]
    if res<dy[i]:
        res =dy[i]
   

print(res)