import sys
from collections import deque
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

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

"""
def h_dfs(x,y):
    if y==9:
        temp=[]
        for i in range(1,10):
            if ch[i] ==0:
                temp.append(i)
        return temp
    else:
        ch[board[x][y]] =1
        h_dfs(x,y+1) 


def v_dfs(x,y):
    if x==9:
        if ch[0]==1:
            return [ch.index(0)]
        else:
            temp=[]
            for i in range(1,10):
                if ch[i] ==0:
                    temp.append(i)
            return temp
    else:
        ch[board[x][y]] =1
        h_dfs(x+1,y) 
dx =[-1,-1,-1,0,0,0,1,1,1]
dy =[-1,0,1,-1,0,1,-1,0,1]

def s_dfs(x,y):
    for i in range(9):
        ch[board[x+dx][y+dy]] =1
    temp=[]
    for i in range(1,10):
        if ch[i] ==0:
            temp.append(i)
    return temp

"""
board=[]
for i in range(9):
    a =list(map(int , sys.stdin.readline().split()))
    board.append(a)


Q = deque()

v_ch = [ [0 for _  in range(10)] for _ in range(10)]

h_ch = [ [0 for _  in range(10)] for _ in range(10)]

for i in range(9):
    for j in range(9):
        v_ch[i][board[i][j]]=1
        h_ch[i][board[j][i]]=1
        if board[i][j]==0:
            Q.append((i,j))
print(v_ch)
print(h_ch)