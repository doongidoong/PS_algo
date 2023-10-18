import sys
from collections import deque
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\samsung\\input.txt","r")
n , m = map(int, input().split())

g = [ list(input()) for _ in range(n) ]

#R, B, O의 위치를 찾음
for i in range(n):
    for j in range(m):
        if g[i][j] == 'R':
            R = (i,j)
        elif g[i][j] == 'B' :
            B = (i,j)   
        elif g[i][j] == 'O' :
            O = (i,j) 

#이동
def GoRight(x,y,m):
    distance = 0
    while y+1<m and g[x][y+1] !='#':
        y=y+1
        if g[x][y] == 'O':
            return (-1,-1,-1)
        distance+=1        
    return (x,y,distance)

def GoLeft(x,y,m):
    distance = 0
    while y-1>=0 and g[x][y-1] !='#':
        y=y-1
        if g[x][y] == 'O':
            return (-1,-1,-1)
        distance+=1        
    return (x,y,distance)

def GoUp(x,y,n):
    distance = 0
    while x-1>=0 and g[x-1][y] !='#':
        x=x-1
        if g[x][y] == 'O':
            return (-1,-1,-1)
        distance+=1        
    return (x,y,distance)

def GoDown(x,y,n):
    distance = 0
    while x+1<n and g[x+1][y] !='#':
        x=x+1
        if g[x][y] == 'O':
            return (-1,-1,-1)
        distance+=1        
    return (x,y,distance)

check = [[[[0] *20 for _ in range(20) ] for _ in range(20) ] for _ in range(20) ]
q =deque()
q.append([R[0],R[1],B[0],B[1],0])

#BFS 
while q:
    x1,y1,x2,y2,move = q.popleft()
    if move == 10:
        print(-1)
        break
    #이미 본 경우 pass
    if check[x1][y1][x2][y2] == 1:
        continue
    check[x1][y1][x2][y2] = 1
    #이전 R, B 위치는 비어둠
    g[R[0]][R[1]] = '.'
    g[B[0]][B[1]] = '.'
    R = (x1,y1)
    B = (x2,y2)
    #새로운 R, B 위치를 채워줌
    g[R[0]][R[1]] = 'R'
    g[B[0]][B[1]] = 'B'
    
    #아래로 이동
    rx, ry, rdis = GoDown(R[0],R[1],n)
    bx, by, bdis = GoDown(B[0],B[1],n)  
    if rdis != 0 or bdis !=0:
        if (bx,by) != (-1,-1): #O를 만난 경우 return (-1,-1,-1)
            if (rx,ry) != (-1, -1):
                if (rx,ry)==(bx,by): # 옮긴 위치가 같은 경우, 
                    if rdis>bdis: #만약 RED 구슬이 더 많이 움직였을 경우 
                        rx-=1 #그만큼 한 칸 위에 있다
                    else:
                        bx-=1
                q.append((rx,ry,bx,by,move+1))
            else:
                print(move+1)
                break

    rx, ry, rdis = GoUp(R[0],R[1],n)
    bx, by, bdis = GoUp(B[0],B[1],n)
    if rdis != 0 or bdis !=0:
        if (bx,by) != (-1,-1):
            if (rx,ry) != (-1, -1):
                if (rx,ry)==(bx,by): # 옮긴 위치가 같은 경우, 
                    if rdis>bdis: #만약 RED 구슬이 더 많이 움직였을 경우 
                        rx+=1 
                    else:
                        bx+=1
                q.append((rx,ry,bx,by,move+1))
            else:
                print(move+1)
                break

    rx, ry, rdis = GoRight(R[0],R[1],m)
    bx, by, bdis = GoRight(B[0],B[1],m)
    if rdis != 0 or bdis !=0:
        if (bx,by) != (-1,-1):
            if (rx,ry) != (-1, -1):
                if (rx,ry)==(bx,by): # 옮긴 위치가 같은 경우, 
                    if rdis>bdis: #만약 RED 구슬이 더 많이 움직였을 경우 
                        ry-=1 #그만큼 한 칸 왼쪽에 있다
                    else:
                        by-=1
                q.append((rx,ry,bx,by,move+1))
            else:
                print(move+1)
                break

    rx, ry, rdis = GoLeft(R[0],R[1],n)
    bx, by, bdis = GoLeft(B[0],B[1],n)
    if rdis != 0 or bdis !=0:
        if (bx,by) != (-1,-1): 
            if (rx,ry) != (-1, -1):
                if (rx,ry)==(bx,by): # 옮긴 위치가 같은 경우, 
                    if rdis>bdis: #만약 RED 구슬이 더 많이 움직였을 경우 
                        ry+=1 #그만큼 한 칸 오른쪽에 있다
                    else:
                        by+=1
                q.append((rx,ry,bx,by,move+1))
            else:
                print(move+1)
                break
else:
    print(-1)

