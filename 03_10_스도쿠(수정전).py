import sys

#sys.stdin = open("input.txt","rt")

L= [list(map(int, input().split())) for i in range(9)]

def check(L):
    for i in range(1,10):
        if i in L:
            continue
        else:
            return False
    return True

def Search_square(L,i,j):
    a=[]
    dx =[-1,-1,-1,0,0,0,1,1,1]
    dy =[-1,0,1,-1,0,1,-1,0,1]
    for k in range(9):
        a.append(L[i+dx[k]][j+dy[k]])
    return check(a)

x = [0,3,6,0,3,6,0,3,6]
y = [0,0,0,3,3,3,6,6,6]

for k in range(9):
    if check(L[k]) and Search_square(L, 1+x[k],1+y[k]) and check([L[i][k] for i in range(9)]) :
        continue
    else:
        print("NO")
        break
else:
    print("YES")