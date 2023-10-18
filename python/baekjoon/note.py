import sys
import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n=int( sys.stdin.readline())
arr =list(map(int,sys.stdin.readline().split()))
dy= [0]*(n)
for i in range(len(arr)):
    maxd= 0
    for j in range(i):
        if arr[i]>arr[j]and maxd<dy[j]:
            maxd= dy[j]
    dy[i]=maxd+1

dy2 = [0]*n
for i in range(len(arr)-1,-1,-1):
    maxd =0
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j] and maxd<dy[j]:
            maxd= dy2[j]
    dy2[i]=maxd+1
dy3=[]

for i in range(n):
    dy3.append(dy[i]+dy2[i]-1)
print(max(dy3))
