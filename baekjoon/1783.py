import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

n, m = map(int, input().split())

if n==1 :
    print(1)
if n==2 :
    print(min((m-1)//2+1,4))

if n>=3:
    if m<=6:
        print(m)
    else:
        print(m-2)


