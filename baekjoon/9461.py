import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
k = int(input())

for i in range(k):
    n = int(input())
    dy=[0,1,1,1,2,2] + [0 for i in range(n-4)]
    for i in range(6,n+1):
        dy[i]= dy[i-5]+dy[i-1]
    print(dy[n])

