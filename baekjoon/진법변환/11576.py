import sys

sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

A,B= map(int, input().split())
m = int(input())
a = list(map(int, input().split()))
n=0
k=1
for  i in a[::-1]:
    n+=i*k
    k*=A
b=[]
while 1:
    b.append(n%B)
    n //= B
    if n==0:
        break
b.reverse()
for i in b:
    print(i,end=' ')