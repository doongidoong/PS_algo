import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n=int(input())
d = {}

for i in range(n):
    k=int(input())
    d[k] = d.get(k,0) +1
maxc=0
res=2**62
for keys,values in d.items():
    if values>maxc:
        maxc=values
        res=keys
    if values == maxc and res>keys:
        res=keys
print(res)


