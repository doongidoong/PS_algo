import sys
#sys.stdin = open("input.txt","rt")


n = int(input())
a = list(map(int,input().split()))
m =  int(input())

def dfs(L,sum):
    global res
    if L>res:
        return
    if sum>m:
        return
    if sum==m:
        res=L
        return
    else:
        for i in range(n):
           dfs(L+1,sum+a[i])
           

a.sort(reverse= True)
res=10000
dfs(0,0)
print(res)

"""
def dfs(V):
    global temp
    if V>m:
        return
    if sum(res)>temp:
        return 
    if V==m:
        temp =sum(res)
        return
    else:
        for i in range(n):
            res[n-i-1]+=1
            dfs(V+a[n-i-1])
            res[n-i-1]-=1          



n = int(input())
a = list(map(int,input().split()))
m =  int(input())
res = [0]*n
temp = 100000000000000
dfs(0)
print(temp)

"""