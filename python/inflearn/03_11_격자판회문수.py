import sys

#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")

L= [list(map(int, input().split())) for i in range(7)]

cnt =0

for i in range(7):
    for j in range(3):
        if L[i][j] == L[i][j+4] and L[i][j+1] == L[i][j+3]:
            cnt+=1
        for k in range(2):
            if L[j+k][i] != L[j+5-k-1][i]:
                break
        else:
            cnt +=1 

print(cnt)


