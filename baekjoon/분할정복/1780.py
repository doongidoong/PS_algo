import sys

sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

n = int(input())

paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


dy= {0:0, -1:0, 1:0 }
def devide(x,y,r):
    check=0
    for i in range(r):
        for j in range(r):
            if paper[x][y] != paper[x+i][y+j]:
                check=1
                break
    if check==1:
        d = r//3
        for i in range(3):
            for j in range(3):
                devide(x+i*d,y+j*d,d)
    else:
        dy[paper[x][y]]+= 1

devide(0,0,n)

print(dy[-1])

print(dy[0])

print(dy[1])