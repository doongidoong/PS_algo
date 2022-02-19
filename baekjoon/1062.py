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
    s = sys.stdin.readline().rstrip()
    for j in s[4:len(s)-3]:
        if check[ord(j)-97]==1:
            continue
        d[i].append(ord(j)-97)


maxc = 0
res=[]
def DFS(L):
    global maxc
    if L == k-5 :
        cnt = n
        for i in range(n):
            for j in d[i]:
                if j in res or j in (0,13,19,8,2):
                    continue
                else:
                    cnt -=1
                    break
        if maxc<cnt:
            maxc = cnt

        return
    else:
        for i in range(26):
            if check[i]==0:
                res.append(i)
                check[i]=1
                DFS(L+1)
                res.pop()
                check[i]=0
DFS(0)
print(maxc)