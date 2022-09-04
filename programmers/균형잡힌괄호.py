p = "(()())()"
answer = ''

def solution(p):
    global answer
    recur(p)
    return answer

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

def divide(p):
    if p:
        left =0
        right = 0
        u =[]
        v = []
        for i in range(len(p)):
            u.append(p[i])
            if p[i]=='(' :
                left+=1
            else:
                right+=1
            if left and left-right == 0:
                for j in range(i+1,len(p)):
                    v.append(p[j])
                break
        return u,v
def recur(p):
    global answer
    if p:
        u,v  = divide(p)
        if check(u)==True:
            answer+= ''.join(u) 
            v = recur(v)
        else : 
            u = make(u)
            answer+= ''.join(u) 
            v = recur(v)


def make(u):
    temp = []
    cnt = 0
    for i in u:
        if i == ')':
            temp.append(')')
            cnt+=1
        else:
            if cnt <= 0 :
                temp.append('(')
                cnt-=1
            if cnt > 0 :
                cnt-=1
                temp.insert(0,'(')
    return ''.join(temp)       
    


print(solution(p))