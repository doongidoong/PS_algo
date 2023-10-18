import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n,m=map(int,input().split())
a = list(sys.stdin.readline().rstrip().split())
a.sort()
res=['']*(n)
check  = ['a','i','e','o','u']

def DFS(L,s,c):
    if L==n:
        if c>= 1 and n-c>=2 :
            for i in res:
                print(i,end='')
            print()
        return
    else:
        for i in range(s,m):
            res[L] = a[i]
            if a[i] in check:
                DFS(L+1,i+1,c+1)
            else:
                DFS(L+1,i+1,c)

DFS(0,0,0)
