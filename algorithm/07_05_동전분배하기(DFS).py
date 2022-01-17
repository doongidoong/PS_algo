import sys

#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","rt")

def DFS(L):
    global res
    if L==n:
        cha = max(money)-min(money)
        if cha <res:
            tmp = set(money)
            if len(tmp) == len(money):
                res=cha
    else:
        for i in range(3):
            money[i] += coin[L]
            DFS(L+1)
            money[i] -= coin[L]
            
n = int(input())
coin =[]
money = [0]*3
res = 2417000000
for _ in range(n):
    coin.append(int(input())) 
DFS(0)
print(res)


"""
내 풀이
n = int(input())

def dfs(L,a,b,c):
    global k
    if L==n:
        if a != b and b!=c and a!=c and k > (max(a,b,c)-min(a,b,c)):
            k= (max(a,b,c)-min(a,b,c))
        return
    else:
        dfs(L+1,a+t[L],b,c)
        dfs(L+1,a,b+t[L],c)
        dfs(L+1,a,b,c+t[L])
k= 10000000
t=[]
for i in range(n):
    p = int(input())
    t.append(p)
dfs(0,0,0,0)
print(k)
"""