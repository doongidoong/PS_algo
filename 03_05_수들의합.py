import sys

sys.stdin  = open("input.txt","rt")

N,M= map(int, input().split())

L = list(map(int, input().split()))

count =0
sumn=0
for i in range(N):
    k=0
    while M-sumn>0:
        sumn += L[i+k]
        if sumn==M:
            count+=1
        k+=1
                    
print(count)