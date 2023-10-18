import sys
from collections import deque
#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")

n,m =  map(int,input().split())

a = list((map(int,input().split())))

a.sort()
# deque 사용 풀이
p = deque(a)
cnt =0
while(p):
    if len(p)==1:
        cnt+=1 
        break
    if p[0]+p[-1]>m:
        p.pop()
        cnt+=1
    else:
        p.popleft()
        p.pop()
        cnt +=1
print(cnt)




"""
내풀이

a.sort(reverse=True)
lt =0
rt =n-1
cnt =0
while(lt<=rt):
    now =0
    cnt+=1
    if m-a[lt]:
        now+=a[lt]
        lt+=1
        while now+a[rt] <= m:
            now+=a[rt]
            rt -=1
print(cnt)

"""
