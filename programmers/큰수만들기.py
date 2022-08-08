def solution(number, k):
    answer = [] # Stack
    stack=[]
    for num in number:
        print('1',answer)
        while k > 0 and answer and answer[-1] < num:
            print('2',answer)
            answer.pop()
            k -= 1
        answer.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(answer[:len(answer) - k])