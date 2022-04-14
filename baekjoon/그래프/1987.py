import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
def to_num(x, y):
    return ord(board[x][y]) - ord('A')
r,c =map(int , sys.stdin.readline().split())
board = [list(map(str, sys.stdin.readline().strip())) for _ in range(r)]

dx=[0,0,1,-1]
dy=[1,-1,0,0]
visited = [0] * 26
visited[to_num(0,0)] = 1

res=1
def DFS(x,y,L):
    global res
    if res<L:
        res=L
    for i in range(4):
        a= x+dx[i]
        b= y+dy[i]
        if a >=r or b >= c or a < 0 or b < 0:
            continue
        if visited[to_num(a,b)] != 1:
            visited[to_num(a,b)] = 1    
            DFS(a,b,L+1)
            visited[to_num(a,b)] = 0
DFS(0,0,1)
print(res)