import sys
def dfs(L, sum):
    global res
    if L>n:
        return
    if L==n:
        if sum >res :
            res =sum
        return
    else:
        dfs(L+a[L][0], sum +a[L][1])
        dfs(L+1,sum)

res = 0


#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","rt")


n = int(input())
a = list(tuple(map(int, input().split())) for _ in range(n))
dfs(0,0)
print(res)

