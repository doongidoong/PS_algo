import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

a = list(map(int,input()))

a.sort(reverse=True)




num=0
s = len(a)-2
lt= s
rt = s
while rt!=0:
    a[lt], a[rt] = a[rt],a[lt]
    for i in a:
        num*=10
        num+=i
    if num%30==0:
        print(num)
        break
    if sum(a)%3 !=0:
        print(-1)
        break
    if lt == rt:
        lt-=1
        rt = s
    else:
        rt-=1
else:
    print(-1)

        