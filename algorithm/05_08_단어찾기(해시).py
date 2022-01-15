import sys
#sys.stdin = open("input.txt","rt")
n = int(input())
d ={}
for i in range(n):
    str = input()
    d[str] = 1

for i in range(n-1):
    str = input()
    d[str] = 0

for key, values in d.items():
    if values>=1:
        print(key)