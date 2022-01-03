import sys



sys.stdin = open("input.txt","rt")

n = int(input())
L = [list(map(int, input().split())) for _ in range(n)]
L.insert(0,[0]*n)
L.append([0]*(n))


for l in L:
    l.insert(0,0)
    l.append(0)
cnt = 0

dx = [-1,0,1,0]
dy = [0,-1,0,1]
for i in range(1,n+1):
    for j in range(1,n+1):
        if all(L[i][j] > L[i+dx[k]][j+dy[k]] for k in range(4)):
            #all은 모두를 만족할때
            cnt +=1 


print(cnt)
