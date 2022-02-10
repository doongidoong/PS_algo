import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n =int(input())
board = [ list(map(int,input().split())) for _ in range(n)]

for i in range(1,n):
    for j in range(i):
        board[i][j] +=board[j][i]
        board[j][i] = 0 

left = [0]*(n//2)
mind = 1e9
def DFS(L,s):
    global mind
    if L==n//2:
        right = []
        for i in range(n):
            if i in left:
                continue
            else:
                right.append(i)
        r = 0
        for i in range(len(left)):
            for j in range(i+1,len(left)):
                r += board[left[j]][left[i]] - board[right[j]][right[i]]
        if abs(r)<mind:
            mind=abs(r)
        return
    else:
        for i in range(s,n):
            left[L]=i 
            DFS(L+1,i+1)

DFS(0,0)
print(mind)