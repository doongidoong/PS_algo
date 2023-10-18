import sys
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")
n=int( sys.stdin.readline())

t = []
p = []
for i in range(n):
    a,b = map(int,  sys.stdin.readline().split())
    t.append(a)
    p.append(b)
answer = 0
def DFS(L,s):
    global answer
    if L>=n:
        if L == n:
            answer = max(answer,s)
        return
    
    DFS(L+t[L],s+p[L])
    DFS(L+1,s)

DFS(0,0)
print(answer)