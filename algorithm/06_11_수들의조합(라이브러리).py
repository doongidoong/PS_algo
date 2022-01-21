from email import iterators
import sys
import itertools as it

#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")

n, k = map(int, input().split())

a = list(map(int,input().split()))

m = int(input())
cnt=0
for tmp in it.combinations(a,k):
    if sum(tmp)%m==0:
        cnt+=1

print(cnt)