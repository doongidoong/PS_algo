import sys

sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

s= sys.stdin.readline().rstrip()
l=[]
for i in range(len(s)):
    l.append(s[i:])
l.sort()

for i in l:
    print(i)
