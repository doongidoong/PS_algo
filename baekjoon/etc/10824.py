
import sys

sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

a,b,c,d= sys.stdin.readline().rstrip().split()

print(int(a+b)+int(c+d))
