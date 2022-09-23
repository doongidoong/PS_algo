a = []
m = 10
while lt<=rt:
    mid=(lt+rt)//2
    if m>a[mid]:
        lt = mid+1
    elif m<a[mid]:
        rt = mid -1
    else:
        print(mid+1)
        break



