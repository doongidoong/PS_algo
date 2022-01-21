import sys
#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")

a , m = input().split()
m= int(m)
num = []
for i in a:
    num.append(int(i))

stack = []
for x in num:
    while stack and m>0 and stack[-1] < x:
        stack.pop()
        m= m-1
    stack.append(x)

if m!= 0:
    stack = stack[:-m]
res = ''.join(map(str,stack))
print(res)