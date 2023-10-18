import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

def r_check(x,num):
    for i in range(9):
        if board[x][i] ==num:
            return False
    return True    

def c_check(y,num):
    for i in range(9):
        if board[i][y] ==num:
            return False
    return True    

def s_check(x,y,num):
    nx= (x//3)*3
    ny = (y//3)*3
    for i in range(3):
        for j in range(3):
            if board[nx+i][ny+j] ==num:
                return False
    return True    

board=[]
for i in range(9):
    a =list(map(int , sys.stdin.readline().split()))
    board.append(a)

Q = []

for i in range(9):
    for j in range(9):
        if board[i][j]==0:
            Q.append((i,j))
def DFS(L):
    if L == len(Q):
        for i in range(9):
            print(' '.join(map(str,board[i])))
        sys.exit(0)
        return 
    else:
        
        for i in range(1,10):
            x= Q[L][0]
            y = Q[L][1]
            if r_check(x,i) and c_check(y,i) and s_check(x,y,i): 
                board[x][y] = i
                DFS(L+1)

DFS(0)
