import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

def DQ(lt,rt):
    if lt == rt:
        return hist[lt]
    mid = (lt+rt)//2

    m = max(DQ(lt,mid), DQ(mid+1,rt))
    m  = max(m, midarea(lt,rt,mid))

    return m

def midarea(lt,rt,mid):
    l = mid
    r = mid
    h = hist[mid]
    area = h
    while l>lt and r< rt:
        if hist[l-1]>hist[r+1]:
            l=l-1
            h=min(h,hist[l])
        else:
            r+=1
            h=min(h,hist[r])
        area = max(area,h*(r-l+1))
    while l>lt:
        l=l-1
        h=min(h,hist[l])
        area = max(area,h*(r-l+1))
    while r<rt:
        r=r+1
        h=min(h,hist[r])
        area = max(area,h*(r-l+1))
    return area



while 1:
    hist = list(map(int,input().split()))
    if hist[0]==0:
        break
    print(DQ(0,len(hist)-1))
    