import sys
#sys.stdin = open("input.txt","rt")
T = int(input())
for t in range(T):
    n, s, e, k = map(int, input().split())
    L = list(map(int, input().split()))
    L = L[s-1:e]
    L.sort()
    print("#{} {}".format(t+1, L[k-1]))
