import sys
sys.stdin = open("input.txt","rt")
n,m = map(int ,input().split())

def dfs(L,S):
    global k
    if L==m:
        for i in p:
            print(i,end =' ')
        print()
        k+=1
                
    else:
        for i in range(S,n+1):
            p[L]= i
            dfs(L+1,i+1)
                

k=0
total =[]
p = [0]*(m)
ch = [0]*(n+1)
dfs(0,1)
print(k)