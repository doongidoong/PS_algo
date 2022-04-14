import sys

sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

def dfs(n,k):
    global s
    if n==0:
        return
    else:
        dfs(n//k,k)
        if (n%k)>=10:
            s+=chr(n%k+55)
        else:
            s+=str(n%k)


s = ''
n, k = map(int,input().split())
dfs(n,k)
if len(s)==0:
    print(0)
else:
    print(s)