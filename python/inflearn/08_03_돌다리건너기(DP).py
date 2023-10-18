# Top-Down : 메모이제이션

import sys

sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")
n = int(input())

dy = [0]*(n+2)
dy[1]=1
dy[2]=2
for i in range(3,n+2):
    dy[i] =dy[i-1]+dy[i-2]
print(dy[n+1])
