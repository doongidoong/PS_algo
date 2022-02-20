import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
T= int(input())
for i in range(T):
    n = int(input())
    member = [0]*(n+1)
    for i in range(n):
        a,b = map(int,input().split())
        member[a]=b
    minrank = n+1
    cnt = 0
    for i in range(1,n+1):
        if minrank > member[i]:
            minrank= member[i]
            cnt+=1
            
    print(cnt)