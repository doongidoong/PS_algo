from cmath import inf
import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

n = int(input())

m = int(input())
if m==0:
    print(min(abs(n-100), len(str(n))))
    sys.exit(0)
else:
    k = list(input().split())
    down=-inf
    for i in range(n,-1,-1):
        for s in str(i):
            if s in k:
                break
        else:
            down=i
            break
    up=inf
    for i in range(n,1000000):
        for s in str(i):
            if s in k:
                break
        else:
            up=i
            break
    print(min(abs(up-n)+len(str(up)),abs(n-down)+len(str(down)),abs(n-100)))
    