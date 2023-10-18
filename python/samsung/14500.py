import sys
from collections import deque
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\samsung\\input.txt","r")

n,m = map(int, input().split())

L = [ list(map(int, input().split())) for _ in range(n)]

first = [[0,0],[1,0],[2,0],[3,0]]
second = [[0,0],[1,0],[0,1],[1,1]]
third = [[0,0],[1,0],[2,0],[2,1]]
fourth = [[0,0],[1,0],[1,1],[2,1]]
fifth = [[0,0],[1,0],[2,0],[1,-1]]
sixth = [[0,0],[1,0],[2,0],[2,-1]]
seventh = [[0,0],[1,0],[1,-1],[2,-1]]
def turn(case, x,y):
    maxNum = 0
    #기본
    temp = 0
    for i in range(len(case)):
        moveX,moveY = case[i]
        xx = x + moveX
        yy = y + moveY
        if 0>xx or xx>= n or 0> yy or yy>= m:
            break
        temp+=L[xx][yy]
    else:
        maxNum = max(temp,maxNum)
    temp = 0
    #오른쪽으로 회전
    for i in range(len(case)):
        moveX,moveY = case[i]
        xx = x - moveY
        yy = y + moveX
        if 0 > xx or xx>= n or 0> yy or yy>= m:
            break
        temp+=L[xx][yy]
    else:
        maxNum = max(temp,maxNum)
    temp = 0
    for i in range(len(case)):
        moveX,moveY = case[i]
        xx = x - moveX
        yy = y - moveY
        if 0> xx or xx>= n or 0> yy or yy>= m:
            break
        temp+=L[xx][yy]
    else:
        maxNum = max(temp,maxNum)
    temp = 0   
    for i in range(len(case)):
        moveX,moveY = case[i]
        xx = x + moveY
        yy = y - moveX
        if 0> xx or xx>= n or 0> yy or yy>= m:
            break
        temp+=L[xx][yy]
    else:
        maxNum = max(temp,maxNum)
    return maxNum

answer = 0
for i in range(n):
    for j in range(m):
        answer= max(turn(first,i,j),turn(second,i,j),turn(third,i,j),turn(fourth,i,j),turn(fifth,i,j),turn(sixth,i,j),turn(seventh,i,j),answer) 

print(answer)