import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
#유클리드 호제법

n1, n2 = map(int, input().split())
n = n1%n2
b= n2
while n!=0:
    a,b = b,n 
    n = a%b
print(b)
print(n1*n2//b)
"""
내 풀이
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

print(cf)
print(a*b//cf)
"""
