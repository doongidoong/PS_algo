import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n , m = map(int,input().split())
dy=[0]*(m+1)
ch = [[0]*(n) for _ in range(m+1)]
for i in range(n):
    a,b = map(int, input().split())
    for j in range(m,a-1, -1): #뒤에서부터 하는 이유는 중복을 피하기 위해
       dy[j] = max(dy[j-a]+b,dy[j])


print(dy)