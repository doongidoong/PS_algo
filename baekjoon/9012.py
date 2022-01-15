import sys
#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n = int(sys.stdin.readline())
for i in range(n):
    stack=[]
    check=0
    a= input()
    for i in a:
        if i =='(':
            stack.append(i)
        else:
            if stack:
                k = stack.pop()
                if k != '(':
                    check=1
                    break
            else:
                check=1
                break
    if len(stack) == 0 and check == 0 :
        print("YES")
    else:
        print("NO")
