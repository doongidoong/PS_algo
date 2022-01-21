import sys

#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")

n= int(input())
a = [ list(map(int,input().split())) for _ in range(n)]

dy=[[0]*n for _ in range(n)]

dy[0][0] =a[0][0]

dy[0][1] =a[0][0] + a[0][1]

dy[1][0] =a[0][0] + a[1][0]
for i in range(0,n):
    for j in range(0,n):
        if j==0:
            k = dy[i-1][j]
        elif i==0 :
            k = dy[i][j-1]
        else:
            k = min(dy[i-1][j],dy[i][j-1])
        dy[i][j] = k+a[i][j]

print(dy[n-1][n-1])


"""
강의 풀이

if __name__=="__main__":
    n=int(input())
    arr=[list(map(int, input().split())) for _ in range(n)]
    dy=[[0]*n for _ in range(n)]
    dy[0][0]=arr[0][0]
    for i in range(1, n):
        dy[0][i]=dy[0][i-1]+arr[0][i]
        dy[i][0]=dy[i-1][0]+arr[i][0]
    for i in range(1, n):
        for j in range(1, n):
            dy[i][j]=min(dy[i-1][j], dy[i][j-1])+arr[i][j]
    print(dy[n-1][n-1])
"""