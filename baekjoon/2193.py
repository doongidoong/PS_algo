import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n = int(input())
dy =[[0,0] for _ in range(91)]
dy[1] =[0,1]
dy[2] =[1,0]
# 0 1 
for i in range(3,n+1):
    dy[i][0]= dy[i-1][1] +dy[i-1][0]
    dy[i][1]= dy[i-1][0] 
    
print(sum(dy[n]))

"""
s = [0, 1, 1]
for i in range(3, 91):
  s.append(s[i - 2] + s[i - 1])
n = int(input())
print(s[n])
"""