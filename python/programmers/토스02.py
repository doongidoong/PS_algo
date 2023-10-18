
def solution(levels):
    ord = int(len(levels)*0.25)
    if(ord==0):
        return max(levels)
    levels.sort(reverse=True)
    answer = levels[ord-1]
    return answer

levels = [1,4,5]

print(solution(levels))


# def solution(levels):
#     levels.sort(reverse=True)
#     tot= len(levels)
#     L = []
#     for i in range(tot):
#         if (i+1)/tot <=0.25:
#             L.append(levels[i])
#     print(L)
#     answer = min(L)
#     return answer

# levels = [1, 2, 3, 4]

# print(solution(levels))