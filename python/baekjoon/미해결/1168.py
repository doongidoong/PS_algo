import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

n, k = map(int, input().split())
dy=[0]*(n+1)
cnt=0
res=[]
t=0
cur=0
print('<',end='')
while cnt<n:
    t+=k
    if t>n :
        t-=n
    if cnt<n-1:
        print(t,end=', ')
    else:
        print(t,end='')
    dy[t]=1
    cnt+=1

print('>')


