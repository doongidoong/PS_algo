import sys
from collections import defaultdict
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

n = int(input())
d=defaultdict(int)

num = []
al  =[0]*26
for i in range(n):
    temp = sys.stdin.readline().rstrip()
    t=1
    num.append(temp)
    for s in temp[::-1]:
        al[ord(s)-ord('A')]+=t
        t*=10
ans = 0
al.sort(reverse = True)
num =9
for j in al:
    ans+=j*num
    num-=1

print(ans)