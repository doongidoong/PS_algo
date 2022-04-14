
import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n,c = map(int,input().split())
a= [ int(input()) for i in range(n)]

a.sort()

def count(distance):
    cnt=1
    now =a[0]
    next = a[1]
    for i in range(1,n):
        next = a[i] 
        if next -now >=distance:
            now = a[i]
            cnt +=1
    return cnt
lt =1
rt = max(a)
res = 0
while lt<= rt:
    mid = (lt+rt)//2
    if count(mid) >= c:
        res = mid
        lt = mid+1
    else:
        rt = mid-1

print(res)