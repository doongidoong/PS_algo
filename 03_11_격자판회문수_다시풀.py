import sys

sys.stdin = open("input.txt","rt")
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






# 내풀이
"""
L.insert(0,[0]*7)
L.append([0]*7)

for i in range(len(L)):
    L[i].insert(0,0)
    L[i].append(0)


cnt =0

for i in range(1,8):
    for j in range(2,7):
        if L[i][j-1] != L[i][j+1]:
            continue
        if L[i][j-2] == L[i][j+2]:
            cnt+=1

for j in range(1,8):
    for i in range(2,7):
        if L[i-1][j] != L[i+1][j]:
            continue
        if L[i-2][j] == L[i+2][j]:
            cnt +=1
print(cnt)
"""