import sys

def reverse(x):
    return int(x[::-1])


def isPrime(x):
    if x==1:
        return False

    for i in range(2,x):
        if (x%i) ==0:
            return False
    return True


#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")

N = int(input())

L = list(input().split())


for i in range(N):
    if isPrime(reverse(L[i])):
        print(reverse(L[i]), end=" ")

