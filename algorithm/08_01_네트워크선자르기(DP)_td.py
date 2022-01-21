#top-down
import sys

sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")

def DFS(L):
    if dy[L]!=0:
        return dy[L]
    if L==2 or L==1:
        return L
    else:
        dy[L]= DFS(L-1)+DFS(L-2)
        return dy[L]

        
n= int(input())

dy = [0]*(n+1)
dy[1]=1
dy[2]=2


print(DFS(n))
