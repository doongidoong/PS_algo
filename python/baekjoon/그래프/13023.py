import sys
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")
m,n = map(int,input().split())
g = [[] for _ in range(m)]

for i in range(n):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

def DFS(L,now):
    if L==4:
        print(1)
        sys.exit()
        return 
    for i in g[now]:
        if check[i]==0:
            check[i]= 1
            DFS(L+1,i)
            check[i]= 0

check= [0]*(m)        
for i in range(m):
    answer = 0
    check[i]=1
    DFS(0,i)
    check[i]=0
print(0)