import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

num = list(input().split())

maxnum =0
minnum= 0
for j in range(2):
    mintemp=0
    maxtemp=0
    for i in num[j]:
        mintemp*=10
        maxtemp*=10
        if i in ('5','6'):
            maxtemp+=6
            mintemp+=5
        else:
            maxtemp+=int(i)
            mintemp+=int(i)
    maxnum+=maxtemp
    minnum+=mintemp
print(minnum,maxnum)