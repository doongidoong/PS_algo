import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
a=int(input())
def s(n):
    if n==3:return['***','* *','***']
    x=s(n//3)
    y=list(zip(x,x,x)) #zip이 순서대로 묶는거임
    for i in range(len(y)):
        y[i]=''.join(y[i])
    
    z=list(zip(x,[' '*(n//3)]*(n//3),x))
    for i in range(len(z)):
        z[i]=''.join(z[i])
    return y+z+y
print('\n'.join(s(a)))

"""
n = int(input())

s = ['***', '* *', '***']

def star():
    global s 
    temp=[]
    for i in range(3):
        for j in s:
            if i==1 :
                temp.append(j+len(j)*' '+j)
            else:
                temp.append(j*3)
    s = temp
k=0
while n!=3:
    n = n//3
    k+=1

for i in range(k):
    star()
for i in s:
    print(i)
"""