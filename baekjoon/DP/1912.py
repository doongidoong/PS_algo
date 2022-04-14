import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n = int(input())
L = list(map(int,input().split()))
dy = [0 for _ in range(n+1)]
L.insert(0,0)
for i in range(1,n+1):
    dy[i]= max(dy[i-1],0)+L[i]

print(max(dy[1:]))