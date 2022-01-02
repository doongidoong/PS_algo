import sys

#sys.stdin = open("input.txt","rt")
N = int(input())
L = list(map(int,input().split()))

sum =0
check =0
for i in L:
    if i==1:
        check+=1
        sum +=check
    else:
        check =0

print(sum)
