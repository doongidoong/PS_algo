import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
k,n = map(int, input().split())
a = list(map(int, input().split()))
    
def count(length):
    res =0
    for i in a:
        res += max(i-length,0)
    return res
lt =0
rt = max(a)
ml =0
while lt<=rt:
    mid = (lt+rt)//2
    if count(mid)>=n:
        if mid>ml:
            ml =mid
        lt = mid+1
    else:
        rt = mid-1
print(ml)
