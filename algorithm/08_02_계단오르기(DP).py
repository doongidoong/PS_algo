# Top-Down : 메모이제이션

import sys

sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")
n = int(input())

dy = [0]*(n+1)
dy[1]=1
dy[2]=2
def DFS(L):
    if dy[L]:
        return dy[L]
    if L<=2:
        return L
    else:
        dy[L]=DFS(L-1) + DFS(L-2)
        return dy[L]
print(DFS(n))
