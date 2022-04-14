import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n = int(input())
dy = [0]*(10001)
L = [int(input()) for _ in range(n)]
L.insert(0,0)
for i in range(1,n+1):
    if i==1:
        dy[i] = L[i]
    if i==2:
        dy[i] = L[i-1]+L[i]
    else:
        dy[i]= max(dy[i-1],dy[i-2]+L[i],L[i-1]+dy[i-3]+L[i])

print(max(dy))