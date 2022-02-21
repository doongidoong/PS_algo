import sys

sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

case= 1
while (1):
    L,P,V = map(int,input().split())
    if (L,P,V) ==(0,0,0):
        break
    ans=0
    temp = V//P
    ans+= temp*L
    ans+= min(L,V-temp*P)
    print("Case %d: %d"%(case,ans))
    case+=1