def solution(triangle):
    dp = [triangle[0]]

    for i in range(1,len(triangle)):
        temp=[]
        for j in range(len(triangle[i])):
            if j==0:
                temp.append(dp[i-1][0]+triangle[i][j])
            elif j==len(triangle[i])-1:
                temp.append(dp[i-1][-1]+triangle[i][j])
            else:
                temp.append(max(dp[i-1][j-1],dp[i-1][j])+triangle[i][j])
        dp.append(temp)
    answer = max(dp[-1])
    return answer


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

solution(triangle)