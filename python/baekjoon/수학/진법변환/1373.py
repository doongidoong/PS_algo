import sys

sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

n = input()[::-1]
res=''
k=0
t = len(n)%3

for i in range(0,len(n)-t,3):
    k=0
    k+= int(n[i])+ int(n[i+1])*2 + int(n[i+2])*4
    res=res+str(k)
s=1
k=0
for i in range(len(n)-t,len(n)):
    k+=int(n[i])*s
    s*=2

res+=str(k)    
    
print(int(res[::-1]))