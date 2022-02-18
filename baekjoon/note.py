import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
a = []
for i in range(9):
    n =int(input())
    a.append(n)
a.sort()
res=[0]*9
def DFS(L,s):
    if L==9:
        if s==100 and sum(res)==7:
            for i in range(9):
                if res[i]==1:
                    print(a[i])
            sys.exit(0)    
        return  
    else:
        res[L]= 1
        DFS(L+1,s+a[L])
        res[L]=0
        DFS(L+1,s)
DFS(0,0)