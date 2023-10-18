import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

n, m, k = map(int, input().split())

while k>0:
    if m>n//2:
        m-=1
    else:
        n-=1
    k-=1

print(m)