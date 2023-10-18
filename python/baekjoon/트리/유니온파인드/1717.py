import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

def find(target):
    if parent[target]==target:
        return target
    parent[target] = find(parent[target])
    return parent[target]

def union(a,b):
    a = find(a)
    b = find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
        

n,m = map(int,sys.stdin.readline().rstrip().split())
parent=[]
for i in range(n+1):
    parent.append(i)

for i in range(m):
    order, a ,b = map(int,sys.stdin.readline().rstrip().split())
    if order==0:
        union(a,b)
    else :
        if find(a)==find(b):
            print("YES")
        else:
            print("NO")