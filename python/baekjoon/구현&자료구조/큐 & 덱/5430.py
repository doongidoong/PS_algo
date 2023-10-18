import sys
from collections import deque
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")


def solution(p,l):
    l = deque(l)
    reverse=-1
    error= -1
    for i in p:
        if i== 'R':
            reverse*=-1
        elif i== 'D':
            if len(l)==0:
                error = 1
                return 'error'
            elif reverse==-1:
                l.popleft()
            else:
                l.pop()
    l = list(l)
    if reverse==1:
        return l[::-1]
    return l
            
T = int(input())
for i in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    a=  sys.stdin.readline().rstrip()[1:-1]
    if ',' in a:
        l = list(map(int, a.split(',')))
    elif len(a)==0:
        l=[]
    else:
        l = [int(a)]
    if n < p.count('D'):
        print("error")
        continue
    answer= solution(p,l)
    if len(answer)==0:
        print('[]')
        continue
    else:
        print("[" + ",".join(list(map(str,answer))) + "]")