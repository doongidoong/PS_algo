import sys

#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")

l = input()

stack =[]

pt = 0
cnt =0
while(pt<len(l)):
    if l[pt]=='(':
        stack.append(l[pt])
    else:
        if stack and l[pt-1]=='(':
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt+=1
    pt+=1
print(cnt)