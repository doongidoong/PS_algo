import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

a, b = map(int ,input().split())
plus = int(input())

hour = (a+(b+plus)//60)%24
minute = (b+plus)%60
print(hour, minute)

