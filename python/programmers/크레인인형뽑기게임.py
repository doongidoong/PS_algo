

boards = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]	

def solution(board,moves):
    stack  =[] 
    answer =0 
    for i in range(len(moves)):
        ind = 0
        a = 0
        loc = moves[i]-1
        if board[len(board)-1][loc] ==0 :
            continue
        
        while True:
            if board[ind][loc] :
                a= board[ind][loc]
                board[ind][loc] = 0
                break
            else :
                ind+=1 

        if stack and stack[-1]==a:
            stack.pop()
            answer+=2
        else:
            stack.append(a)
    return answer

print(solution(boards,moves))