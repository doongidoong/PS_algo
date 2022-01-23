import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")

cnt =0 
def dfs(L):
    global cnt 
    if L==n:
        cnt+=1
        return
    else:
        for i in range(1, n+1):
            for j in range(L):
                if i== res[j] or abs(i-res[j])== L-j:
                    break
            else:
                res[L]=i
                dfs(L+1)
                


if __name__ =="__main__" :
    n = int (input())
    res =[0]*(n)
    ch = [0]*(n+1)
    dfs(0)
    print(cnt)