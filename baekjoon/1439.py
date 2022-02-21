import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

L = list(map(int,sys.stdin.readline().rstrip()))
if len(L)==0 :
    print(0)
    sys.exit(0)
s=0
lt = 0
cnt1=0
cnt2=0
while lt<len(L):
    if L[lt]==s:
        cnt1+=1
        while lt< len(L) and L[lt]==s:
            lt+=1
    else:
        cnt2+=1
        while lt< len(L) and L[lt]!=s:
            lt+=1

print(min(cnt1,cnt2))