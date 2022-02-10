import sys
#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

e,s,m= map(int,input().split())

a=1
b=1
c=1
cnt=1
if e==1 and s==1 and m==1 :
    print(1)
    sys.exit(0)
while(1):
    cnt+=1
    a= min(a+1,(a+1)%16 +1)
    b = min(b+1,(b+1)%29 +1)
    c=  min(c+1,(c+1)%20 +1)
    if a==e and b==s and c==m:
        print(cnt)
        break