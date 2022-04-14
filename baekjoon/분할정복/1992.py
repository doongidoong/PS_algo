import sys

sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

n = int(input())

image = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
s=''
def devide(x,y,r):
    global s
    check=0
    for i in range(r):
        for j in range(r):
            if image[x][y] != image[x+i][y+j]:
                check=1
                break
    if check==1:
        s+='('
        d = r//2
        for i in range(2):
            for j in range(2):
                devide(x+i*d,y+j*d,d)
        s+=')'
    else:
        s+= str(image[x][y])

print(image)
devide(0,0,n)

print(s)