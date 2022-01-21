import sys

#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")

n = int(input())

sumlist =[]

L = [list(map(int,input().split())) for i in range(n)] # 리스트 컴프리헨션

dianum1 = 0
dianum2 = 0

for i in range(n):
    num1 =0
    num2 =0
    dianum1+=L[i][i]
    dianum2+=L[i][n-1-i]
    for j in range(n):
        num1+=L[i][j]
        num2+=L[j][i]
    sumlist.append(max(num1,num2))
sumlist.append(max(dianum1,dianum2))
print(max(sumlist))