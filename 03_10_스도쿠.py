import sys

#sys.stdin = open("input.txt","rt")

L= [list(map(int, input().split())) for i in range(9)]


def check(L):
    for i in range(9):
        ch1 = [0]*10
        ch2 = [0]*10
        for j in range(9):
            ch1[L[i][j]] =1
            ch2[L[j][i]] =1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False
    for i in range(3):
        for j in range(3):
            ch3 = [0]*10
            for k in range(3):
                for s in range(3):
                    ch3[L[3*i+k][3*j+s]] =1
            if sum(ch3) != 9:
                return False
    return True    

if check(L):
    print("YES")
else:
    print("NO")