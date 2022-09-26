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


def lower_bound(begin, end, target_list, target):
    if begin >= end:
        return begin    
    mid = (begin + end) // 2
    if target_list[mid] >= target:
        return lower_bound(begin, mid, target_list, target)
    else:
        return lower_bound(mid+1, end, target_list, target)
