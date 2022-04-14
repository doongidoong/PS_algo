import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
sys.setrecursionlimit(10**6)
n = int(input())
a= list(map(int, input().split()))
ch=[0]*n
maxd =-1000000
def DFS(L,pre,end,s):
    global maxd
    if L==n-1:
        if s>maxd:
            maxd=s
        return
    else:
        for i in range(n):
            if ch[i]==0:
                ch[i]=1
                DFS(L+1,end,a[i],s+abs(end-a[i]))
                ch[i]=0

for i in range(n):
    for j in range(n):
        ch[i]=1
        ch[j]=1
        DFS(1,a[i],a[j],abs(a[i]-a[j]))
        ch[i]=0
        ch[j]=0
print(maxd)
