import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

Ax, Ay, Bx, By, Cx, Cy, Dx, Dy = map(int,input().split())


k1 =  (Dx-Cx)/ (Bx-Ax)

k2 = (Dy-Cy) /(By-Ay)

t = 0.0000001
n=1
nx= Ax
ny = Ay
a=10000

"""
print(k1,k2)
while nx<Bx and ny < By:
    nx = Ax+t
    ny = Ay+t
    print( t*k1*(k1 - 2*(Cx-Ax)) + t*k2*(k2 - 2*(Cy-Ay)))
    if a > t*k1*(k1 - 2*(Cx-Ax)) + t*k2*(k2 - 2*(Cy-Ay)):
        a = t*k1*(k1 - 2*(Cx-Ax)) + t*k2*(k2 - 2*(Cy-Ay))
    t=n*t
    n+=1
print(a)
"""