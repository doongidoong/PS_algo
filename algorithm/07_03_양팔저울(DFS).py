import sys

#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","rt")

def dfs(L, w):
    if L==n:
        if w>=0:
            ch[w]=0
        return
    else:
        dfs(L+1,w+a[L])    
        dfs(L+1,w)
        dfs(L+1,w-a[L])

n = int(input())
a = list(map(int, input().split()))
a.sort()
ch = [1]*(sum(a)+1)
dfs(0,0)
print(sum(ch))  