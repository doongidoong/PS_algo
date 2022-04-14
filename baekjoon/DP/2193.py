import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n = int(input())
dy =[[0,0] for _ in range(91)]


"""
s = [0, 1, 1]
for i in range(3, 91):
  s.append(s[i - 2] + s[i - 1])
n = int(input())
print(s[n])
"""