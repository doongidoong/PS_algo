def solution(nums):
    length= len(nums)
    inputSet = set(nums)
    answer = min(length/2, len(inputSet))
    return answer
