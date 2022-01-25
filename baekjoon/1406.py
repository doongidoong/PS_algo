import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

s = input()
stack =[]
temp =[]

for  i in s:
    stack.append(i)

n = int(input())


for i in range(n):
    a = list( map(str, sys.stdin.readline().split()))
    if a[0]=='P':
        for k in a[1]:
            stack.append(k)
    elif a[0]=='L' and stack:
        t= stack.pop()
        temp.append(t)
    elif a[0]=='D' and temp:
        t= temp.pop()
        stack.append(t)
    elif a[0]=='B' and stack:
        stack.pop()
for j in stack:
    print(j,end='')
for j in range(len(temp)):
    print(temp.pop(),end='')
