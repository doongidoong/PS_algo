from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def solution(board):
    q = deque()
    q.append((0,0,0,-1))
    distance = [[[10000000 for _ in range(len(board))] for _ in range(len(board))],[[10000000 for _ in range(len(board))] for _ in range(len(board))]]
    distance[0][0][0] = 0
    distance[1][0][0] = 0   
    lb = len(board)
    while q:
        x,y, c, r = q.popleft()
        for i in range(4):
            cost = 100
            xx = x + dx[i]
            yy = y + dy[i] 
            if xx<0 or xx> len(board)-1 :
                continue
            if yy<0 or yy> len(board)-1 :
                continue
            if board[xx][yy]==1:
                continue
            if dx[i] != 0 :
                if r == 0  :
                    cost +=500
                road = 1        
            if dy[i] != 0 :
                if r == 1 :
                    cost += 500
                road = 0
            if distance[road][xx][yy] > c + cost:
                distance[road][xx][yy] = c + cost
                q.append((xx,yy,c+cost,road))
    answer = min(distance[0][lb-1][lb-1],distance[1][lb-1][lb-1] )         

    return answer
