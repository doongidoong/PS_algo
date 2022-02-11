import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

n = int(input())
a=[]
for i in range(n):
    A,B = map(int, input().split())
    a.append((A,B))

a.sort()
dy=[0]*(n)
maxd=0
dy[0]=1
for i in range(1,len(a)):
    maxd=0
    for j in range(i):
        if a[i][1]>a[j][1] and maxd<dy[j]:
            maxd=dy[j]
    dy[i] =maxd+1

print(n-max(dy))