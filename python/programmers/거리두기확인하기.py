from collections import deque
dx  = [1,0,-1,0]
dy  = [0,1,0,-1]
check = [[0,0,0,0,0] for i in range(5) ]
places= []
def solution(place):
    global answer
    global places
    places = place
    answer = [1 for i in range(len(places))]
    for k in range(len(places)):
        for i in range(5):
            for j in range(5):
                now = places[k][i][j] 
                if now=='P':
                    check[i][j]= 1
                    DFS(0,i,j,k)
                    check[i][j]= 0

    return answer
res = []
def DFS(L,x,y,room):
    if L>=2 :
        return
    for i in range(4):
        xx =x + dx[i]
        yy= y + dy[i]
        if xx >=0 and yy >= 0 and xx<5 and yy<5 and check[xx][yy] == 0 :
            if places[room][xx][yy] == 'P':
                answer[room] = 0
                return
            if places[room][xx][yy] == 'O':
                check[xx][yy] = 1
                DFS(L+1, xx,yy,room)
                check[xx][yy] = 0

