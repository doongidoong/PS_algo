import sys

sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")

n= int(input())

L =[]

for i in range(n):
    m = int(input())
    if m==0:
        L.pop()
    else:
        L.append(m)

print(sum(L))