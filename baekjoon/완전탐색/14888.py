import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

n = int(input())

num= list(map(int,input().split()))

d= list(map(int,input().split()))


maxd= -1e9
mind = 1e9

def DFS(L,total, a,b,c,d):
    global maxd, mind
    if L==n:
        maxd = max(total, maxd)
        mind = min(total, mind)
        return
    else:
        if a>=1:
            DFS(L+1,total+num[L],a-1,b,c,d)
        if b>=1:
            DFS(L+1,total-num[L],a,b-1,c,d)
        if c>=1:
            DFS(L+1,total*num[L],a,b,c-1,d)
        if d>=1:
            DFS(L+1,int(total/num[L]),a,b,c,d-1)

DFS(1,num[0],d[0],d[1],d[2],d[3])

print(maxd)

print(mind)