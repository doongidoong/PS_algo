import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

n = int(input())
dy = [[0]*10 for _ in range(n+1)]
for i in range(1,10):
    dy[1][i] = 1

for j in range(2,n+1):
    for i in range(10):
        if i==0:
            dy[j][0]= dy[j-1][1]
        elif i==9:
            dy[j][9]= dy[j-1][8]
        else:
            dy[j][i] = dy[j-1][i-1] +dy[j-1][i+1]
    
print(sum(dy[n])%1000000000)
