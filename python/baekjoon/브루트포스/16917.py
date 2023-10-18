import sys
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")

a,b,c,x,y = map(int,input().split())
ans = 0
if a+b > 2 * c:
    if a>2*c and b>2*c:
        temp = max(x,y)
    elif b > 2 * c:
        temp = y
    elif a> 2*c :
        temp = x
    else:
        temp = min(x,y)
    ans = temp*c*2
    x = max(x-temp,0)
    y = max(y-temp,0)
    ans += x*a + y*b
else:
    ans += x*a + y*b
print(ans)