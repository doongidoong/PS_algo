import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
dy =[0 for _ in range(101)]
n = int(input())
a = list(map( int , input().split()))
dy[1]= a[0]

if n==1:
    print(dy[1])
    sys.exit(0)
for i in range(2,n+1):
    k = a[i-1]
    for j in range(i+1//2):
        k = max(k,dy[j]+dy[i-j])
    dy[i] = k

print(dy[n])