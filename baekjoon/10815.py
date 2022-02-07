import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

n = int(input())

a  = list(map(int , input().split()))

nc =[0 for _ in range(10000000)]    
mc =[0 for _ in range(10000000)]    

for i in a:
    if i > 0:
        nc[i] =1
    if i < 0 :
        mc[-1*i]=1

k = int(input())

b  = list(map(int , input().split()))

for i in b:
    if i>0:
        print(nc[i],end=' ')
    if i<0 :
        print(mc[-1*i],end=' ')
