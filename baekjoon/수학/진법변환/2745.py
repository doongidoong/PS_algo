import sys

sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

n, k = sys.stdin.readline().split()
k = int(k)
d={}
for i in range(10,36):
    d[chr(i+55)] = i
s=0
for i in n:
    s*=k
    if d.get(i,0) >0 :
        s+= d.get(i)
    else:
        s+=int(i)


print(s)