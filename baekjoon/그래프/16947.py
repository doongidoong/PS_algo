import sys
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")
    
n = int(input())

g= [[0]*(n+1) for _ in range(n+1)]

for i in range(n):
    a,b =map(int,input().split())
    g[a][b] = 1
    g[b][a] = 1

print(g)
p =[-1]*(n+1)
def find(a):
    while p[a]>0:
        a= p[a]
    return a

def union(a,b):
    ta = find(a)
    tb = find(b)
    if ta>tb:
        p[tb] += p[ta]
        
        p[ta] = tb
    else:
        print(ta)
        p[ta] += p[tb]
        p[tb] = ta

union(1,2)
print(p)