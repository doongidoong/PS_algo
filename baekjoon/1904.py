import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n =int(input())
limit = 1000000	
dy = [0]* 1000

dy[1]=1
dy[2]=2

for i in range(3,1000001):
    dy[i] = (dy[i-1]+dy[i-2])%15746

print(dy[n])