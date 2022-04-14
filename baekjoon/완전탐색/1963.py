from cmath import inf
import sys
from collections import deque

def R(s):
    new = s % 10 * 1000 + s // 10
    return int(new)
def L(s):
    new = s % 1000 * 10 + s / 1000
    return int(new)

def D(s):
    return (2*s)%10000

def S(s):
    val = s-1
    if val == -1:
        val =9999
    return val
    
 
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
T = int(input())

for i in range(T):
    A, B = map(int, sys.stdin.readline().strip().split(' '))
    dy= ['' for _ in range(10001)]
    visit = [ 0 for _ in range(10001) ]
    Q=deque()
    Q.append(A)
    visit[A] = 1 
    while Q:
        p = Q.popleft()
        if p == B:
            print(dy[p])
            break
        new1 = D(p)
        if visit[new1] ==0:
            visit[new1]=1
            dy[new1] = dy[p]+'D'
            Q.append(new1)
        new2 = S(p)
        if visit[new2] ==0:
            visit[new2]=1
            dy[new2] = dy[p]+'S'
            Q.append(new2)
        new3= L(p)
        if visit[new3] ==0:
            visit[new3]=1
            dy[new3] = dy[p]+'L'
            Q.append(new3)
        new4 = R(p)
        if visit[new4] ==0:
            visit[new4]=1
            dy[new4] = dy[p]+'R'
            Q.append(new4)
