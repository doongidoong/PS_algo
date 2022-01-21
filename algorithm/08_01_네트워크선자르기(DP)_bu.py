#bottom-up
import sys

#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")

n= int(input())

dy = [0]*(n+1)
dy[1]=1
dy[2]=2
for i in range(3,n+1):
    dy[i]= dy[i-1]+dy[i-2]

print(dy[n])