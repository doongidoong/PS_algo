def solution(s):
    answer = True
    stack =[]
    for i in s:
        if i=='(':
            stack.append(i)
        else :
            if stack :
                a = stack.pop()
                if a!='(':
                    return False
            else:
                return False
    if stack:
        return False
    return True

s	=")()("
print(solution(s))