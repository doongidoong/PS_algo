import sys
#sys.stdin = open("input.txt","rt")
n = int(input())



def transform(num):
    if num//2 ==0:
        return str(num)
    else:
        return str(transform(num//2))+str(num%2)

print(transform(n))