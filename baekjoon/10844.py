import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
#DP 문제 계단 쌓기
n = int(input())
dy = [[0]*10 for _ in range(n+1)]
for i in range(1,10): #dy[1]일때 각 숫자 1~9까지 만들어질 수 있는 경우를 구한다
    dy[1][i] = 1

for j in range(2,n+1):
    for i in range(10):
        if i==0: # 0일때는 1이 감소하는 경우밖에 없다
            dy[j][0]= dy[j-1][1]
        elif i==9: # 9일때 또한 8이 증가하는 경우밖에 없다
            dy[j][9]= dy[j-1][8]
        else:
            dy[j][i] = dy[j-1][i-1] +dy[j-1][i+1]
    
print(sum(dy[n])%1000000000)
