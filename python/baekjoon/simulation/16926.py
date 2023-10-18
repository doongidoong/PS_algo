import sys

sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")

n,m,r = map(int, input().split())

L = [list(map(int, input().split())) for _ in range(n)]

command = list(map(int,input().split()))



for t in range(r):
    com = command[t]
    if com == 1:
        L = L[::-1]

    if com == 2:
        for i in range(len(L)):
            L[i] = L[i][::-1]

    if com == 3:
        temp=[]
        for j in range(len(L[0])):
            rowtemp =[]
            for i in range(len(L)-1,-1,-1):
                rowtemp.append(L[i][j])
            temp.append(rowtemp)
        L= temp
    if com == 4:
        temp=[]
        for j in range(len(L[0])-1,-1,-1):
            rowtemp =[]
            for i in range(len(L)):
                rowtemp.append(L[i][j])
            temp.append(rowtemp)
        L= temp

    if com == 5:
        temp=[]
        
        for i in range(len(L)//2,len(L)):
            rowtemp =[]
            for j in range(len(L[0])//2):
                rowtemp.append(L[i][j])
            for j in range(len(L[0])//2):
                rowtemp.append(L[i-len(L)//2][j])
            temp.append(rowtemp)
        
        for i in range(len(L)//2,len(L)):
            rowtemp =[]
            for j in range(len(L[0])//2, len(L[0])):
                rowtemp.append(L[i][j])
            for j in range(len(L[0])//2, len(L[0])):
                rowtemp.append(L[i-len(L)//2][j])
            temp.append(rowtemp)
        L= temp

    if com == 6:
        temp=[]
        
        for i in range(len(L)//2,len(L)):
            rowtemp =[]
            for j in range(len(L[0])//2, len(L[0])):
                rowtemp.append(L[i-len(L)//2][j])
            for j in range(len(L[0])//2, len(L[0])):
                rowtemp.append(L[i][j])
            
            temp.append(rowtemp)
        
        for i in range(len(L)//2,len(L)):
            rowtemp =[]
            for j in range(len(L[0])//2):
                rowtemp.append(L[i-len(L)//2][j])
        
            for j in range(len(L[0])//2):
                rowtemp.append(L[i][j])
            
            temp.append(rowtemp)
        L= temp


for i in range(len(L)):
    print(' '.join(map(str,L[i])))