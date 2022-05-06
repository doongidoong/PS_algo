import sys
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")

T = int(input())
MAXN = 1000000

dy = [0 for _ in range(MAXN+1)] 
dy[1] =1
dy[2] = 2

dy[3] = 2 + 1 + 1  # 111 12 21 3  

for i in range(4,MAXN+1):
    dy[i]= (dy[i-1]+dy[i-2]+dy[i-3])%1000000009

for i in range(T):
    n = int(input())
    print(dy[n]%1000000009)
