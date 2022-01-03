import sys

sys.stdin  = open("input.txt","rt")

N,m= map(int, input().split())

L = list(map(int, input().split()))

cnt =0
tot=L[0]
lt =0
rt =1


while 1:
    if tot < m:
        if rt<N:
            tot += L[rt]
            rt +=1
        else:
            break
    elif tot ==m:
        tot -= L[lt]
        lt +=1
        cnt +=1
    else:
        tot -= L[lt]
        lt +=1
            
print(cnt)