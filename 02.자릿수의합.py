import sys
def digit_sum(x):
    x = str(x)
    sumd =0
    for i in x:
        sumd+= int(i)
    return sumd

#sys.stdin = open("input.txt","rt")

N = int(input())
L = list(map(int, input().split()))
digitL = list()
for i in L:
    digitL.append(digit_sum(i))

print(L[digitL.index(max(digitL))])