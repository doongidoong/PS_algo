import sys

#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")
N = int(input())

rootN = int(N**(0.5))+1

L = [0]*(N+1)
for i in range(2,rootN+1):
    for j in range(2*i,N+1,i):
        L[j] = 1

count =0
for i in range(N+1):
    if L[i]==1:
        count +=1 
print(N-count-1)


