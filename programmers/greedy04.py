from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    people= deque(people)
    while people:
        answer+=1
        if len(people)>=2 and people[0]+people[-1]<= limit:
            people.popleft()
            people.pop()
        else:
            people.pop()   


        

    return answer

people= [70, 80, 50]	
limit=100
solution(people,limit)