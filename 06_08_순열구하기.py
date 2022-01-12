import sys
#sys.stdin = open("input.txt","rt")
cnt =0 
def dfs(L):
    global cnt
    if L==m:
        for i in res:
            print(i, end=' ')
        print()
        cnt+=1
        return
    else:
        for i in range(1,n+1):
            if ch[i]==1:
                continue
            res[L]=i
            ch[i]=1
            dfs(L+1)
            ch[i]-=1



if __name__ =="__main__" :
    n,m = map(int ,input().split())
    res =[0]*(m)
    ch = [0]*(n+1)
    dfs(0)
    print(cnt)