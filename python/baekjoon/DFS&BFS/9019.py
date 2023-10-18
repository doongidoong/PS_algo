from cmath import inf
import sys
from collections import deque

def c_replace(s,i,index):
    new = s[:index]+i +s[index+1:]
    return new

sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n = int(input())

for i in range(n):
    s,t = input().split()
    prime = [0]*10000
    prime[1] =1
    prime[0] =1
    for i in range(2,101):
        for j in range(2*i,10000,i):
            prime[j]=1
    Q =deque()
    Q.append(s)
    dy = [inf]*10000
    dy[int(s)] =0
    while Q:
        p = Q.popleft()
        val =dy[int(p)]
        for j in range(0,4):
            for i in range(0,10):
                new = c_replace(p,str(i),j)
                if int(new) >= 1000 and prime[int(new)] == 0 and dy[int(new)]>val+1:
                    dy[int(new)] = val+1
                    Q.append(new)
    print(dy[int(t)])