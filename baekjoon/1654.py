import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
k,n = map(int, input().split())
a=[]
for i in range(k):
    t= int(input())
    a.append(t)

def count(length):
    res =0
    for i in a:
        res += i//length
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
    
