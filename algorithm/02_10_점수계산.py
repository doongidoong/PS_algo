import sys
#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")

N = int(input())
L = list(map(int,input().split()))

sum =0
check =0
for i in L:
    if i==1:
        check+=1
        sum +=check
    else:
        check =0

print(sum)
