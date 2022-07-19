
leftCase= [1,4,7]
rightCase = [3,6,9]

def getDistance(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])


def solution(numbers, hand):
    answer = ''
    lpos = [3,0]
    rpos = [3,2]
    for num in numbers:
        if num in leftCase:
            answer+='L'
            lpos = [(num-1)//3,0]
        elif num in rightCase:
            answer+='R'
            rpos = [(num-1)//3,2]
        else:
            if num== 0:
                numPos =[3,1]
            else:
                numPos = [(num-1)//3,1]
            if getDistance(lpos,numPos) < getDistance(rpos,numPos):
                answer+='L'
                lpos = numPos
            elif getDistance(lpos,numPos) > getDistance(rpos,numPos):
                answer+='R'
                rpos = numPos
            else:
                if hand !='right':
                    answer+='L'
                    lpos = numPos
                else:
                    answer+='R'
                    rpos = numPos
    return answer
        
