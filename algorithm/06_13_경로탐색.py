import sys

#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")

def dfs(v):
    global cnt 
    if v==n:
        cnt+=1
        #for x in path: 
        #    print(x,end = ' ')  경로 출력
        return
    else:
        for i in range(1,n+1):
            if ch[i] ==0 and g[v][i]==1:
                ch[i] =1 
                path.append(i)
                dfs(i)
                path.pop()
                ch[i] = 0 


n , m = map(int,input().split())
g = [[0]*(n+1) for _ in range(n+1)]
ch = [0]*(n+1)
for i in range(m):
    a, b = map(int,input().split())
    g[a][b] = 1


cnt =0
path = []  # 해당 문제에서는 필요없지만 경로를 알아보기위해 넣음
path.append(1)
ch[1]=1
dfs(1)
print(cnt)