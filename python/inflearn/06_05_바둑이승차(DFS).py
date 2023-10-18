import sys

#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")

def dfs(L,sum, tsum):
    global result, total
    if (sum + (total - tsum)) < result : # 전체합 - 판단을 한 값 = 앞으로 판단해야할 무게값
        return                           # 이게 지금까지 구한 result보다 작다면 굳이 계산할 필요X
    if sum > c:
        return
    if L == n:
        if sum > result:
            result = sum
        return
    else:
        dfs(L+1, sum+a[L], tsum+a[L]) # tsum은 부분집합에 넣던 넣지 않았던 판단한 값
        dfs(L+1, sum, tsum+a[L])      
        

if __name__ =="__main__" :
    c,n = map(int ,input().split())
    a = [ int(input()) for _ in range(n) ]
    total = sum(a)
    result = -2140000000
    dfs(0,0,0)
    print(result)

# 내풀이
"""
temp=0
def dfs(index,sum):
    global temp 
    if (sum) < c:
        if temp < (sum):
            temp = sum
        return
    if sum < temp or index ==n:
        return
    else:
        dfs(index+1, sum-a[index])
        dfs(index+1, sum)

c,n = map(int ,input().split())
a = [ int(input()) for _ in range(n) ]
total = sum(a)

dfs(0,total)

print(temp)

"""
