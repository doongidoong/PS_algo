import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n=int( sys.stdin.readline())
t=[]
p=[]
for i in range(n):
    a,b = map(int,  sys.stdin.readline().split())
    t.append(a)
    p.append(b)
dy=[0]*(n+1)


if t[n-1] == 1:
    dy[n-1] = p[n-1]
    
for i in range(n-1,-1,-1):
    if i+t[i]>n:
        dy[i]=dy[i+1]
    else:
        dy[i]= max(dy[i+1],dy[i+t[i]]+p[i])
print(max(dy))
