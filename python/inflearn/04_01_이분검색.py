import sys

def search(a,m,lt,rt):
    mid = (lt+rt)//2
    if m>a[mid]:
        return search(a,m,mid+1,rt)
    elif m<a[mid]:
        return search(a,m,lt,mid-1)
    else:
        return (lt+rt)//2

#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")

n ,m = map(int,input().split())
a = list(map(int,input().split()))

a.sort()
lt = 0
rt = n-1

while lt<=rt:
    mid=(lt+rt)//2
    if m>a[mid]:
        lt = mid+1
    elif m<a[mid]:
        rt = mid -1
    else:
        print(mid+1)
        break



