import sys
sys.stdin = open("input.txt", "rt")

def count(capa):
    cnt = 1
    sumc =0
    for x in a:
        if sumc+x > capa:
            cnt += 1
            sumc =x
        else:
            sumc+= x
    return cnt


n, m = map(int,input().split())
a = list(map(int,input().split()))

lt=a[0]
rt=sum(a)

res = 0
maxx = max(a)
while lt<=rt:
    mid = (lt+rt)//2
    if mid >= maxx and count(mid) <=m:
        res =mid
        rt = mid-1
    else:
        lt = mid+1


print(res)
