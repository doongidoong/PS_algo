import sys
#sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\baekjoon\\input.txt","rt")

d = {}
answer =[]
n,m = map(int , input().split())
for i in range(n):
    s= sys.stdin.readline().rstrip()
    d[s]=1
cnt = 0 
for i in range(m):
    s = sys.stdin.readline().rstrip()
    if d.get(s,0)==1:
        cnt+=1
        answer.append(s)
answer.sort()
print(cnt)
for i in answer:
    print(i)

