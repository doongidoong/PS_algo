import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n = int(input())
dy = [0]*(n)
L = list(map(int,input().split()))
dy[0]= L[0]

for i in range(1,n):
    maxd=0
    for j in range(i):
        if L[j]<L[i] and maxd<dy[j]:
            maxd = dy[j]        
    dy[i] = maxd+L[i]
print(max(dy))