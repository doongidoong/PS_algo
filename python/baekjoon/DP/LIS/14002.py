import sys
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")

n = int(input())
L = list(map(int,input().split()))
dy = [0 for i in range(n)]
l = [[] for i in range(n)]
target = -1
for i in range(n):
    maxd= 0
    temp = []
    for j in range(i):
        if L[i]>L[j] and dy[j]>maxd:
            maxd = dy[j]
            temp = l[j]
    l[i] = temp + [L[i]]
    dy[i] = maxd+1
k = max(dy)
print(k)
for i in l[dy.index(k)]:
    print(i,end=' ')

