import sys

#sys.stdin  = open("input.txt","rt")

N = int(input())
a = list(map(int, input().split()))

N2 = int(input())
b = list(map(int, input().split()))


# 이미 정렬되어잇으므로 굳이 다시 정렬할 필요없

ll = []
p1 =0
p2 =0 
while p1<N and p2 <N2:
    if a[p1]<= b[p2]:
        ll.append(a[p1])
        p1+=1
    else:
        ll.append(b[p2])
        p2+=1
if p1<N:
    ll = ll + a[p1:]
if p2<N:
    ll = ll + b[p2:]
for i in ll:
    print(i, end = ' ')