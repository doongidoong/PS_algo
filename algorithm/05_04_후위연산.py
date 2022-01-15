import sys

sys.stdin =  open("input.txt", "rt")


a = input()
stack =[]

temp=0

for x in a:
    if x.isdecimal():
        stack.append(int(x))
    else:
        if x=='+':
            tmp = stack[-2]+stack[-1]
        elif x=='-':
            tmp = stack[-2]-stack[-1]
        elif x=='*':
            tmp = stack[-2]*stack[-1]
        elif x=='/':
            tmp = stack[-2]/stack[-1]
        stack.pop()
        stack.pop()
        stack.append(tmp)

print(stack[0])