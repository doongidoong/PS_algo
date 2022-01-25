import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")


n = int(input())
dy = [[0]*10 for _ in range(n+1)]
for i in range(0,10):
    dy[1][i] = 1


for i in range(2,n+1):
    for j in range(10):
        if j ==0 :
            dy[i][j] =sum(dy[i-1])
        else:
            dy[i][j] = dy[i][j-1] - dy[i-1][j-1]
print(sum(dy[n]))