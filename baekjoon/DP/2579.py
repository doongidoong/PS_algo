import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n = int(input())
L = list(int(input()) for _ in range(n))
L.insert(0,0)
dy = [0 for _ in range(n+1)]
dy[1] = L[1]
for i in range(2,n+1):
    if i==2:
        dy[2] = dy[1]+L[2]
    elif i==3:
        dy[3] = max(L[2]+L[3], L[1]+L[3])
    elif i==4:
        dy[4] = max(L[1]+L[2], L[1]+L[3])+L[4]
    else:
        dy[i]= max(L[i-1]+dy[i-3],dy[i-2])+L[i]


print(dy[n])