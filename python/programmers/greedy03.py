def solution(number, k):
    answer = [] # Stack
    
    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
    if k != 0:
        stack = stack[:len(stack)-k]
    return ''.join(answer[:len(answer) - k])