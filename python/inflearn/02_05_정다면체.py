import sys


#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")

A, B = map(int, input().split())

L = [0]*(A+B+2)

for i in range(1,A+1):
    for j in range(1,B+1):
        L[i+j] +=1

for i in range(1,len(L)):
    if L[i] ==max(L):
        print(i, end=" ")