import sys
from collections import defaultdict
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")


n,k = map(int, sys.stdin.readline().split())
d = defaultdict(list)
check = [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]

if k<5:
    print(0)
    sys.exit(0)
if k==26:
    print(n)
    sys.exit(0)

for i in range(n):
    d[i] = set(sys.stdin.readline().rstrip())
    
maxc = 0

def DFS(idx,L):
    global maxc
    if L == k-5 :
        cnt = n
        for i in range(n):
            for j in d[i]:
                if check[ord(j)-97] == 0:
                    cnt -=1
                    break
        if maxc<cnt:
            maxc = cnt
        return
    else:
        for i in range(idx,26):
            if check[i]==0:
                check[i]=1
                DFS(i,L+1)
                check[i]=0
DFS(0,0)
print(maxc)