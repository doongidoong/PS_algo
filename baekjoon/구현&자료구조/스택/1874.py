import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

n = int(input())

L = list(int(input()) for _ in range(n))
stack = []
answer = []
for i in range(1,n+1):
    answer.append('+')
    stack.append(i)
    while stack and stack[-1] == L[0]:
        answer.append('-')
        stack.pop()
        L.pop(0)

if L :
    print("NO")
else:
    for i in answer:
        print(i)
    