import sys
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")
m,n = map(int,input().split())
g = [[] for _ in range(m)]

for i in range(n):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

def DFS(L,now):
    if L==n:
        return 
    for i in g[now]:
        if check[i]==0:
            check[i]= 1
            DFS(L+1,i)
            
cnt=0
check= [0]*(m)        
for i in range(m):
    if check[i]==0:
        check[i]=1
        DFS(0,i)
        cnt+=1
print(cnt)