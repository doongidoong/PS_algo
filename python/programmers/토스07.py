answer = 0

def solution(money, stocks):
    global checked
    checked= [0]*len(stocks)
    DFS(money,stocks,0)
    return answer


def DFS(money,stocks,earn):
    global answer
    for i in range(len(stocks)):
        if checked[i]==0 and money >=stocks[i][1]:
            checked[i]=1
            DFS(money-stocks[i][1],stocks,earn+(stocks[i][0]))
            checked[i]=0
    answer = max(answer,earn)
money=10
stocks=[[1, 1], [3, 5], [3, 5], [4, 9]]