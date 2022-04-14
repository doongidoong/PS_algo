n = int(input())

s =0
e = n-1
for i in range(n):
    if i==0:
        for j in range(n-1):
            print(' ',end='')
        print('*')
    elif i==n-1:
        for j in range(2*n-1):
            print('*',end='')
    else:
        for j in range(n-1-i):
            print(' ',end='')
        print('*',end='')
        for s in range(2*i-1):
            print(' ',end='')
        print('*')


