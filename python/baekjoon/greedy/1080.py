import sys

sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")


def reverse(h,v):
    for i in range(h,h+3):
        for j in range(v,v+3):
            if A[i][j] == '0':
                A[i][j]='1'
            else:
                A[i][j]='0'

n, m = map(int, input().split())

A = []
for  i in range(n):
    s = list(map(str,input()))
    A.append(s)
B=[]
for  i in range(n):
    s = list(map(str,input()))
    B.append(s)

cnt=0
for j in range(m-2):
    for i in range(n-2):
        if A[i][j] != B[i][j]:
            cnt+=1
            reverse(i,j)
if A==B:
    print(cnt)
else:
    print(-1)