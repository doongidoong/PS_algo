import sys

sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

n, m = map(int, input().split())

setmin  =1001
indmin = 1001
for i in range(m):  
    a,b = map(int, input().split())
    setmin = min(a,setmin)  
    indmin = min(b,indmin)
ans=0
c=0
if setmin >indmin*6 :
    ans+=n*indmin
else:
    ans += (n//6)*setmin
    c = n%6
    ans+= min(setmin,c*indmin)

print(ans)