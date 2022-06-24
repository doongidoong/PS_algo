import sys
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")


s = input()

prev= s[0]

if s[0]=='d':
    k=10
    prev='d'
if s[0]=='c':
    k=26
    prev='c'
for i in range(1,len(s)):
    if s[i]=='c' :
        now=26 
    if s[i]=='d' :
        now=10
    if s[i]==prev:
        now-=1
    k = k*now
    prev=s[i]
print(k)
