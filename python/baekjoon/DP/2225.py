import sys
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")
n,k = map(int,input().split())
s=7
dy = [[0]*s for j in range(s)]

for i in range(s):
    dy[1][i] = 1
    dy[2][i] = i+1
    
for i in range(3,s):
    for j in range(s):
        dy[i][j] = dy[i-1][j]+ dy[i][j-1]
print(dy[k][n]%1000000000)