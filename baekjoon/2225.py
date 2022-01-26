
import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n,k = map(int,input().split())
s=201
dy = [[0]*s for j in range(s)]

for i in range(s):
    dy[1][i] = i
    dy[i][1] = i

for i in range(2,s):
    for j in range(s):
        dy[j][i]  = dy[j-1][i] + dy[j][i-1]

print(dy[k][n]%1000000000)