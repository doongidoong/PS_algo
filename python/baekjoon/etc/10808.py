import sys

sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
d=[0]*26
s = sys.stdin.readline().strip()

for i in s:
    d[ord(i)-97] +=1

for i in d:
    print(i,end=' ')
