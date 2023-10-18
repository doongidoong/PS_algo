import sys

sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")


def fact(n):
    if n<=2:
        return n
    else:
        return n*fact(n-1)


n = int(input())

s = str(fact(n))
k=0
for i in s[::-1]:
    if i=='0':
        k+=1
    else:
        break
if n==0:
    print(0)
    
else:
    print(k)
