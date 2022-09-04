p = "()))((()"	
def divide(p):
    if p:
        left =0
        right = 0
        u =[]
        v = []
        for i in range(len(p)):
            if p[i]=='(' :
                left+=1
            else:
                right+=1
            if left and left-right == 0:
                return p[:i + 1], p[i + 1:]

def check(u):
    temp = []
    for i in u:
        if i== '(':
            temp.append(i)
        else:
            if temp and temp[-1] == '(':
                temp.pop()
            else:
                return False
    return True


def solution(p):
    # 과정 1
    if not p:
        return ""

    # 과정 2
    u, v = divide(p)

    # 과정 3
    if check(u):
        # 과정 3-1
        return u + solution(v)
    # 과정 4
    else:
        # 과정 4-1
        answer = '('
        # 과정 4-2
        answer += solution(v)
        # 과정 4-3
        answer += ')'

        # 과정 4-4
        for p in u[1:len(u) - 1]:
            if p == '(':
                answer += ')'
            else:
                answer += '('

        # 과정 4-5
        return answer

print(solution(p))