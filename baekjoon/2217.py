import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
a.sort()
weight = 0
for i in range(len(a)):
    if weight< a[i]*(n-i):
        weight =a[i]*(n-i)

print(weight)
