import sys


#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")
N, K = map(int, input().split())

L = list(map(int, input().split()))

sumlist = []

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            sumn = L[i]+L[j]+L[k]
            if sumn in sumlist:
                continue
            else:
                sumlist.append(sumn)
sumlist.sort(reverse=True)
print(sumlist[K-1])

