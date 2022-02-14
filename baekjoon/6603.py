import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

def DFS(L,s):
    if L == 6:
        print(' '.join(map(str,res)))
        return
    else:
        for i in range(s,g[0]):
            res[L]= g[i+1]
            DFS(L+1,i+1)
while 1:
    g = list(map(int, sys.stdin.readline().strip().split()))
    if g[0]==0:
        break
    res = [0]*(6)
    for j in range(g[0]-6+1):
        res[0]=g[j+1]
        DFS(1,j+1)
    print()
