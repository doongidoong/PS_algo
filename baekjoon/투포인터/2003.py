import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n,s = map(int, sys.stdin.readline().strip().split())
g = list(map(int, sys.stdin.readline().strip().split()))

lt=0
rt=0
num = g[0]
cnt = 0
while 1:
    if num < s:
        rt+=1
        if rt== n:
            break
        num += g[rt]
    else:
        if num == s:
            cnt+=1
        num -= g[lt]
        lt+=1
print(cnt)

