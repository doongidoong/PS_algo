import sys

sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")

n= int(input())
a = list(map(int,input().split()))
a.insert(0,0)
dy = [0]*(n+1)
dy[1]=1
res=0
for i in range(2,n+1):
    maxd=0
    for j in range(i-1,0,-1):
        if a[j]<a[i] and dy[j]>maxd:
            maxd= dy[j]
    dy[i] = maxd+1
    if res<dy[i]:
        res=dy[i]

print(res)

