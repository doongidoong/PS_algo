import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

n = int(input())

a  = list(map(int , input().split()))

d={}
for i in a:
    d[i] = d.get(i,0) +1

k = int(input())

b  = list(map(int , input().split()))

for i in b:
    print(d.get(i,0), end=' ')