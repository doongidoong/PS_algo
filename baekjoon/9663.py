import sys

cnt =0 
def dfs(L):
    global cnt 
    if L==n:
        cnt+=1
        return
    else:
        for i in range(1, n+1):
            res[L]=i
            for j in range(L):
                if res[L]== res[j] or abs(i-res[j])== L-j:
                    break
            else:
                
                dfs(L+1)
                


if __name__ =="__main__" :
    n = int (input())
    res =[0]*(n)
    dfs(0)
    print(cnt)