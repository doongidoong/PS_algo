import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n = int(input())
dy =[0,1,3]
for i in range(3,n+1):
    dy.append(dy[i-1]+2*dy[i-2])

print(dy[n]%10007)