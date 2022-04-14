import sys
a,b = map(int ,sys.stdin.readline().split())
sumnum = (b*(b+1)/2)-((a-1)*(a)/2)  

print(int(sumnum))