import sys

#sys.stdin  = open("input.txt","rt")

N = int(input())
L = list(map(int, input().split()))

N2 = int(input())
L2 = list(map(int, input().split()))
for i in L2:
    L.append(i)

L.sort()

for i in L:
    print(i, end = ' ')