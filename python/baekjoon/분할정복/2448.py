import sys
#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
a=int(input())
def t(n):
    if n==3:return['  *  ',' * * ','*****']
    x = t(n//2)
    y= list(zip(x,x))
    s = ' '*((n//2))
    s2 = ' '
    for i in range(len(x)):
        x[i] = s + x[i] + s
    for i in range(len(y)):
        y[i]=s2.join(y[i])
    return x+y
L= t(a)
for i in L:
    print(i)

