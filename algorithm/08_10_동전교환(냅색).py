import sys

sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")

n = int(input())

a = list(map(int , input().split()))

m = int(input())
dy = [m]*(m+1)
dy[0]=0
for i in a:
    for j in range(i,m+1):
        dy[j] = min(dy[j-i]+1,dy[j])

print(dy[-1])