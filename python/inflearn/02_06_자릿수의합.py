import sys
def digit_sum(x):
    x = str(x)
    sumd =0
    for i in x:
        sumd+= int(i)
    return sumd

#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")

N = int(input())
L = list(map(int, input().split()))
digitL = list()
for i in L:
    digitL.append(digit_sum(i))

print(L[digitL.index(max(digitL))])