m,n = map(int,input().split())
L = list(map(int,input().split()))

L.sort(reverse=True)

print(L[n-1])