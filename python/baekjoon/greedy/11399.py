import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n = int(input())
a = list(map(int,input().split()))

a.sort()

k = 0
tot =0
for i in a:
    k+=i
    tot+=k
print(tot)
