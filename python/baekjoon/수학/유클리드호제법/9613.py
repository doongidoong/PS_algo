import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

def GCD(a,b):
    m = a%b
    while m>0:
        a, b = b,m
        m = a%b
    return b 

n = int(input())

for i in range(n):
    res = 0
    L = list(map(int,input().split()))
    for i in range(1,L[0]+1):
        for j in range(i+1,L[0]+1):
            res+=GCD(L[i],L[j])
    print(res   )

     