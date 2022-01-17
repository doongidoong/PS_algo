import sys

#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","rt")

def dfs(L, w):
    if L==n:
        if w>=0:
            ch[w]=0
        return
    else:
        dfs(L+1,w+a[L])    
        dfs(L+1,w)
        dfs(L+1,w-a[L])

n = int(input())
a = list(map(int, input().split()))
a.sort()
ch = [1]*(sum(a)+1)
dfs(0,0)
print(sum(ch))  


"""강의 풀이
def DFS(L,sum):
    global res
    if L==n:
        if 0<sum<=s :
            res.add(sum) 
    else: 
        DFS(L+1, sum+G[L])
        DFS(L+1, sum-G[L])
        DFS(L+1, sum)

if __name__ == "__main__":
    n= int(input())
    G = list(map(int, input().split()))
    s = sum(G)
    res = set()
    DFS(0,0)
    print(s-len(res))

"""