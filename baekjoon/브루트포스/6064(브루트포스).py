#카잉달력
import sys
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")

t = int(input())



for i in range(t):    
    a = 0
    b = 0
    m,n,x,y = map(int, input().split())
    while a<m*n:
        if ((a + x)-y)%n ==0:
            break 
        a +=m
    else:
        print(-1)
        continue
    print(a+x)


