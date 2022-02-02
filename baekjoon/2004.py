import sys

sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

def count2(n):
    k=0
    while n!=0:
        n = n//2
        k+=n
    return k

def count5(n):
    k=0
    while n!=0:
        n = n//5
        k+=n
    return k

n,m = map(int,input().split())

print(min(count2(n) - count2(n - m) - count2(m), count5(n) - count5(n - m) - count5(m)))
