import sys



# sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\algorithm\\input.txt","rt")

n = int(input())
L = [list(map(int, input().split())) for _ in range(n)]
L.insert(0,[0]*n)
L.append([0]*(n))
for i in L:
    i.insert(0,0)
    i.append(0)

cnt = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        now = L[i][j]
        left = L[i][j-1]
        right = L[i][j+1]
        up  = L[i-1][j]
        down  = L[i+1][j]
        if now > max(left, right, up, down):
            cnt+=1
print(cnt)