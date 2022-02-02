#홀수만 고려
import sys

sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

dy = [0]*(1000001)
dy[1]=1

for i in range(3,10001,2):
    for j in range(3*i,1000001,2*i):
        dy[j]=1

while 1:
    n=int(input())
    if n==0:
        break
    for i in range(3,(n//2)+1,2):
        if dy[i]== 0 and dy[n-i]==0:
            break
    else:
        print("Goldbach's conjecture is wrong.")
        continue
    print("{} = {} + {}".format(n,i,n-i))
        
"""
전체 고려 pypy 통과
import sys

#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

dy = [0]*(1000001)
dy[1]=1

for i in range(2,10001):
    for j in range(2*i,1000001,i):
        dy[j]=1

while 1:
    n=int(input())
    if n==0:
        break
    for i in range(3,(n//2)+1,2):
        if dy[i]== 0 and dy[n-i]==0:
            break
    else:
        print("Goldbach's conjecture is wrong.")
        continue
    print("{} = {} + {}".format(n,i,n-i))
        

"""