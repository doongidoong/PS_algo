import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n,m = map(int,input().split())
a= list(map(int,input().split()))
b = list(map(int,input().split()))

for i in b:
    lt =0
    for j in range(lt,len(a)):
        if a[j]> i:
            a.insert(j,i)
            lt = j
            break
if len(a)<n+m:
    a += b[(n+m)-len(a):]
for i in a:
    print(i,end= ' ')