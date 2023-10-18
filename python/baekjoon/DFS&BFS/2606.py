import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
node = int(input())

n = int(input())

g = [[] for i in range(node+1)]
for i in range(n):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)
ch =[0]*(node+1)
def DFS(L,i):
    if L == n:
        return
    else:
        for i in g[i]:
           if ch[i]==0 :
               ch[i]=1
               DFS(L+1,i)
DFS(0,1)
print(sum(ch)-1)
