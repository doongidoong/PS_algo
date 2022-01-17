import sys

#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","rt")

def dfs(L,sum):
    global cnt
    if sum>t:
        return
    if L == k:
        if sum ==t:
            cnt +=1
        return
    else:
        for i in range(tp[L][1]+1):
            dfs(L+1,sum + i*tp[L][0])
            
cnt =0
t = int(input())

k = int(input())
tp = []
for i in range(k):
    p,n = map(int,input().split())
    tp.append((p,n))
tp.sort(reverse=True)
  
dfs(0,0)
print(cnt)
"""
def DFS(L,sum):
    global cnt
    if L ==k:
        if sum ==T:
            cnt +=1
    else:
        for i in range(cn[L]+1):
            DFS(L+1,sum + i*cv[L])

if __name__ == "__main__":
    T = int(input())
    k = int(input())
    cv = list()
    cn = list()
    for i in range(k):
        a, b = map(int , input().split())
        cv.append(a)
        cn.append(b)
    cnt =0
    DFS(0,0)
    print(cnt)
"""