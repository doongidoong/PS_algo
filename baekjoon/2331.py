import sys
from collections import deque
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

def mult(n,p):
    k=0
    while n>0:
        t=1
        for i in range(p):
            t*=n%10
        k+=t
        n= n//10
    return k

a, p = map(int,input().split())
cycle = []
cycle.append(a)
while cycle:
    n = cycle[-1]
    t= mult(n,p)
    if t in cycle:
        print(cycle.index(t))
        break
    else:
        cycle.append(t)