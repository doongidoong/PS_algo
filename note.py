n, m = map(int,input().split())
L  = list(map(int,input().split()))

cnt = 0

answer=0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            sumL = L[i]+L[j]+L[k]
            if sumL<=m:
                if sumL>answer:
                    answer=sumL


print(answer)
