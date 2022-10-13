import sys
from collections import deque, defaultdict

dx =[1,-1,0,0]
dy =[0,0,1,-1]

def solution(map):
    answer = 0
    cnt=0
    Q = deque()
    maps = []
    for i in map:
        l = []
        for j in i:
            l.append(j)
        maps.append(l)
    n = len(maps)
    m = len(maps[0])
    check = [[0]*m for _ in range(n)]
    for p1 in range(n):
        for p2 in range(m):
            if maps[p1][p2]!='.' and check[p1][p2] == 0:
                Q.append((p1,p2))
                d = defaultdict(list)
                dcnt = defaultdict(int)
                check[p1][p2]=1
                d[maps[p1][p2]].append((p1,p2))
                dcnt[maps[p1][p2]] = 1
                while Q:
                    p = Q.popleft()
                    for i in range(4):
                        a = p[0]+dx[i]
                        b = p[1]+dy[i]
                        if 0<=a<=n-1 and 0<=b<=m-1 and check[a][b] == 0 and maps[a][b]!='.':
                            check[a][b]=1
                            d[maps[a][b]].append((a,b))
                            dcnt[maps[a][b]] +=1
                            Q.append((a,b))
                maxKey = ''
                maxCnt = 0
                for key, value in dcnt.items():
                    if maxCnt <= value:
                        if maxCnt == value:
                            if ord(maxKey) < ord(key):
                                maxKey = key
                            maxCnt = value
                        else:
                            maxCnt = value
                            maxKey = key
                for key, valueList in d.items():
                    if dcnt[key] < maxCnt : 
                        for x,y in valueList:
                            maps[x][y] = maxKey
    total = defaultdict(int)
    for p1 in range(n):
        for p2 in range(m):
            if maps[p1][p2]!='.':
                total[maps[p1][p2]] +=1
    print(total)
    answer = 0
    for key, value in total.items():
        answer =max(answer,value)
    return answer

solution(
["AABCA.QA", "AABC..QX", "BBBC.Y..", ".A...T.A", "....EE..", ".M.XXEXQ", "KL.TBBBQ"])