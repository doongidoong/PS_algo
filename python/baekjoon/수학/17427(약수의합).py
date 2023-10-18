import sys


sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")
n= int(input())

rang = 1000001
dy= [0]*rang



for i in range(1,rang):
    temp=0
    for j in range(i,rang,i):
        dy[j]+=i
    dy[i]+= dy[i-1]
print(dy[n])
