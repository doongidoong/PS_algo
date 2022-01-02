import sys
import copy


#sys.stdin = open("input.txt","rt")

N = int(input())
L = list(map(int,input().split()))
avg = int(round((sum(L))/ len(L),0))
L2 = list()
for i in range(N):
    L2.append(abs(L[i] -avg))
m = min(L2)
num = 0
for i in range(N) :
    if L2[i] == m:
        if num<L[i]:
            num = L[i]
print(avg, L.index(num)+1)
