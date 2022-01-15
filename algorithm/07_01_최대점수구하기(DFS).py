import sys

#sys.stdin = open("input.txt","rt")

def dfs(L, sum,time):
    global res
    if L==n:
        if res < sum and time <= m:
            res =sum
        return
    else :
        dfs(L+1, sum+pv[L],time+pt[L])
        dfs(L+1, sum,time)
        
    
       

n,m = map(int, sys.stdin.readline().split())
pv =list()
pt = list()
for i in range(n):
    a , b = map(int, sys.stdin.readline().split())
    pv.append(a)
    pt.append(b)
res=0


dfs(0,0,0)
print(res)