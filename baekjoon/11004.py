import sys
from collections import deque
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

"""
def Qsort(lt,rt):
    if lt<rt:
        pos =lt
        pivot =rt
        for i in range(lt,rt):
            if a[i]<a[pivot]:
                a[pos],a[i] = a[i],a[pos]
                pos+=1
        a[pos],a[pivot] = a[pivot],a[pos]
        Qsort(lt,pos-1)
        Qsort(pos+1,rt)
   

"""
n,k = map( int , sys.stdin.readline().split())

a = list(map( int , sys.stdin.readline().split()))
for i in range(k):
    s=min(a)
    a.remove(s)

print(s)


