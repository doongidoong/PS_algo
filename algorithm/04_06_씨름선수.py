import sys
#sys.stdin = open("input.txt", "rt")
n = int(input())

L = []

for i in range(n):
    a,b =map(int, input().split())
    L.append((a,b))


L.sort(reverse=True)

weight=0
cnt = 0
for i in range(n):
    if weight < L[i][1]:
        weight = max(weight ,L[i][1])
        cnt +=1
    else:
        continue
print(cnt)
