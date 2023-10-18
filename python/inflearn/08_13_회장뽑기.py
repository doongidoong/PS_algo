import sys
#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")

n = int(input())
dis = [[51]*(n) for _ in range(n)]


for i in range(0,n):
    dis[i][i] =0
while 1:    
    a, b= map(int,input().split())
    if a==-1:
        break
    dis[a-1][b-1]= 1
    dis[b-1][a-1]= 1


for k in range(0, n):
    for i in range(0, n):
        for j in range(0, n):
            dis[i][j]=min(dis[i][j], dis[i][k]+dis[k][j])

res =[]
for i in range(n):
    res.append(max(dis[i]))
tot=[]
for i in range(n):
    if min(res)==res[i]:
        tot.append(i)

print(min(res), len(tot))
for i in tot:
    print(i+1, end= ' ')

"""
강의 풀이

if __name__=="__main__":
    n=int(input())
    dis=[[100]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dis[i][i]=0
    while True:
        a, b=map(int, input().split())
        if a==-1 and b==-1:
            break
        dis[a][b]=1
        dis[b][a]=1

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dis[i][j]=min(dis[i][j], dis[i][k]+dis[k][j])

    res=[0]*(n+1)
    score=100
    for i in range(1, n+1):
        for j in range(1, n+1):
            res[i]=max(res[i], dis[i][j])
        score=min(score, res[i])
    out=[]
    for i in range(1, n+1):
        if res[i]==score:
            out.append(i)
    print("%d %d" %(score, len(out)))
    for x in out:
        print(x, end=' ')

"""