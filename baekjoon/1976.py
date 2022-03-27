import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

def find(target):
    if parent[target]== target:
        return target
    parent[target] = find(parent[target])
    return parent[target]

def union(a,b):
    a= find(a)
    b= find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

n= int(input())

parent=[]
for i in range(n):
    parent.append(i)

m = int(input())
for i in range(n):
    L = list(map(int,input().split()))
    for j in range(n):
        if L[j]==1:
            union(i,j)
L = list(map(int,input().split()))
temp = []
for i in L:
    temp.append(find(i-1))
if len(set(temp))==1:
    print("YES")
else:
    print("NO")
