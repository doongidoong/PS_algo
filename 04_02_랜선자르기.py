import sys
sys.stdin = open("input.txt", "rt")

def count(len):
    cnt =0
    for i in L:
       cnt += i//mid
    return cnt
n,m = map(int, input().split())
L = [int(input()) for i in range(n)]

rt = max(L)
lt = 0
res = 0
while(lt<=rt):
    mid = (lt+rt)//2
    if count(mid) >= m:
        lt = mid +1
        res = mid
    else :
        rt = mid-1

print(res)

