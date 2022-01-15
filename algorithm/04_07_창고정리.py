import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
a = list(map(int,input().split()))
m = int(input())
cnt=0
a.sort(reverse=True)

while(cnt<m):
    while(a[0]>=a[1] and a[-1]<=a[-2]):
        a[0] -=1
        a[-1] +=1
        cnt+=1
    s=0
    e=0
    while(a[0]<a[s+1]):
        s+=1
    a[0], a[s] = a[s], a[0]
    while(a[n-1]>a[n-2-e]):
        e+=1
    a[-1], a[n-1-e] = a[n-1-e], a[-1]
    
print(a[0]-a[n-1])


