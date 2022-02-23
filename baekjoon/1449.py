import sys

sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

n,L = map(int,input().split())

a = list(map(int,input().split()))
a.sort()
end = 0
cnt = 0
for i in range(n):
    if a[i] > end :
        cnt+=1
        end = a[i]+L-0.5

print(cnt)