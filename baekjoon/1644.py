import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n=int(input())
limit = 4000000
prime = [1]*(4000002)
prime[1]=0
prime[0]=0
for i in range(2,2001):
    for j in range(2*i,4000002,i):
        prime[j]= 0

if n<2:
    print(0)
    sys.exit(0)

lt =2
rt= 2
tot = 2
anw=0
while(1):
    if tot<n:
        while rt<=n:
            rt+=1
            if rt >=n+1:
                print(anw)
                sys.exit(0)
            if prime[rt]==1:
                tot+=rt
                break
    else:
        if tot == n:
            anw +=1
        tot -=lt
        while 1:
            lt+=1 
            if prime[lt]==1:
                break        
