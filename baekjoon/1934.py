import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")


n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    n1 = min(a,b)
    n2 = max(a,b)
    rootn = int(n1**(0.5))
    cf = 1

    for i in range(1,rootn+1):
        if n1%i == 0 and n2%i == 0 and cf<i:
            cf=i
        if n1%i == 0 and n2%(n1//i) == 0 and cf<(n1//i):
            cf = (n1//i)
    print(a*b//cf)

