import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n =int(input())
a= [ list(map(int,input().split())) for _ in range(n)]

if n==1:
    print(a[0][0])
    sys.exit(0)
dy = [a[0][0]+a[1][0],a[0][0]+a[1][1]]
if n==2:
    print(max(dy))
    sys.exit(0)
else:
    for i in range(2,n):
        temp=[]
        temp.append(dy[0]+a[i][0])
        for j in range(1,i):
            temp.append(max(dy[j-1],dy[j])+a[i][j])
        temp.append(dy[i-1]+a[i][-1])
        dy=temp

print(max(dy))