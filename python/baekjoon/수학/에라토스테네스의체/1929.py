import sys

sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

m,n= map(int, input().split())

dy = [0]*(n+1)
dy[1]=1
rn = int(n**(0.5))+1

for i in range(2,rn):
    for j in range(2*i,n+1,i):
        dy[j]=1

for i in range(m,n+1):
    if dy[i]==0:
        print(i)
