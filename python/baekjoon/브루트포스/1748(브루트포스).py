import sys

sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")

n= int(input())

k = len(str(n))
ans =0
t= 1
s= 0

if n<10:
    print(n)
    sys.exit(0)

while t < k :
    ans += 9*(10**(t-1))*(t)
    t+=1
    
ans+=(n+1-10**(t-1))*t
print(ans)

