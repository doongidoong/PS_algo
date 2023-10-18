def solution(routes):
    routes.sort(key= lambda x: x[1])
    e=routes[0][1]
    cnt=1
    for i in range(1,len(routes)):
        if routes[i][0]<=e:
            continue
        else:
            e=routes[i][1]
            cnt+=1
    answer = cnt
    return answer
routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]

solution(routes)