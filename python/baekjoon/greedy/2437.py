import sys

sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n=int(input())
a = list(map(int,input().split()))

a.sort()

print(a)
