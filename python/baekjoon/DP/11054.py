import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n = int(input())

L = list(map(int,input().split()))
fdy =[0 for i in range(n)]
bdy =[0 for i in range(n)]
dy = [0 for i in range(n)]
for i in range(n):
    for j in range(i):    
        if L[i]>L[j] and fdy[i]<fdy[j]:
            fdy[i] =fdy[j]
    fdy[i]+= 1
    
for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if L[i]>L[j] and bdy[i]<bdy[j]:
            bdy[i] =bdy[j]
    bdy[i] +=1


for i in range(n):
    dy[i] = fdy[i] + bdy[i] - 1


print(max(dy))
            
