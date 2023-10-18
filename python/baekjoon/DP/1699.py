import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n = int(input())
dy = [0 for _ in range(n+1)]
dy[1]=1

for i in range(2,n+1):
    mind = n
    for j in range(1,int(i**0.5)+1):
        if mind>dy[i-(j**2)]:
            mind= dy[i-(j**2)]
            
    dy[i]=mind+1

print(dy[n])