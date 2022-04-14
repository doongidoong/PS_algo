import sys

sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

n,k = map( int , sys.stdin.readline().split())

a = list(map( int , sys.stdin.readline().split()))
a.sort()
print(a[k-1])


