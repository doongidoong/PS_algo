import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")



n1, n2 = map(int, input().split())
n = n1%n2
b= n2
while n!=0:
    a,b = b,n 
    n = a%b
print('1'*b)


