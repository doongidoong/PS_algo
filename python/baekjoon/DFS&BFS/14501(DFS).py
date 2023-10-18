import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n=int( sys.stdin.readline())
t=[]
p=[]
for i in range(n):
    a,b = map(int,  sys.stdin.readline().split())
    t.append(a)
    p.append(b)
maxd = 0 
def DFS(L,s):
    global maxd
    if L>n:
        return
    if L==n:
        maxd = max(s,maxd)
        return
    else:
        DFS(L+1,s)
        DFS(L+t[L],s+p[L])
DFS(0,0)
print(maxd)