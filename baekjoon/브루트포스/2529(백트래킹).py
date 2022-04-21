
import sys

sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")
n = int(input())
a = list(map(str, sys.stdin.readline().split()))
check = [0 for _ in range(10)]
answer1= '9876543210'
answer2= '0'

def DFS(l,s,t):
    global answer1,answer2
    if l==n:
        if int(answer1) >int(t):
            answer1=t
        if int(answer2) <int(t):
            answer2= t
        return
    if a[l]=='<':
        for i in range(10):
            if check[i]==0 and s<i:
                check[i]=1
                DFS(l+1,i,t+str(i))
                check[i]=0
    elif a[l]=='>':
        for i in range(10):
            if check[i]==0 and s>i:
                check[i]=1
                DFS(l+1,i,t+str(i))
                check[i]=0
for i in range(0,10):
    check[i]=1
    DFS(0,i,str(i)) 
    check[i]=0

print(answer2)
print(answer1)