def getArea(hs,he,vs,ve):
    ans = 0
    for i in range(hs,he+1):
        for j in range(vs,ve+1):
            ans += a[i][j]
    return ans

import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

n,m = map(int, input().split())
a= [ list(map(int, input())) for _ in range(n) ]
tot=0
for i in range(n):
    for j in range(m):
        tot+=a[i][j]

r = 0
first=0
second =0
third = 0
for i in range(n-1): # 세로, 세로 끝에 닿기 전까지
    for j in range(m): # 가로 
        if j == m-1: # 첫 사각형이 가로로 가득 찬 직사각형, 가장 위가 가로로 가득 찼으므로 남은 부분을 세로로 할지 가로로 할지임
            first=getArea(0,i,0,m-1) # i행까지의 가로로 가득찬 직사각형 넓이
            #남은 부분을 가로로 긴 직사각형으로 나눔
            for k in range(i+1,n): # i+1행부터 세로 길이를 1씩 늘려감 
                second = getArea(i+1,k,0,m-1) # 가로로 긴 사각형
                third = tot-first-second
                if r< first*second*third:
                    r = first*second*third
            #남은 부분을 세로로 나눔
            for k in range(0,m-1):
                second = getArea(i+1,n-1,0,k) #세로로 나눠야하므로 가장 위의 사각형을 제외한 나머지 길이까지
                third = tot-first-second
                if r< first*second*third:
                    r = first*second*third
        else:   
            first=getArea(0,i,0,j) # 이제 가로로 한 개씩 경우를 알아봄
            second=getArea(0,i,j+1,m-1) # 모두 직사각형이야하므로 가로를 무조건 다 채워야함, 같은 높이의 직사각형을 오른쪽으로 만듦
            third = tot-first-second
            if r< first*second*third:
                r = first*second*third
            second=getArea(0,n-1,j+1,m-1) # 남은 가로 길이에다가 세로로 끝까지 채운 직사각형을 오른쪽에 만든 케이스
            third = tot-first-second
            if r< first*second*third:
                r = first*second*third

for i in range(0,m-2): #세로로 가득찬 유형
    first=getArea(0,n-1,0,i) 
    for j in range(0,n): # 남은 부분을 가로로 절단
        second =getArea(0,j,i+1,m-1)
        third = tot-first-second
        if r< first*second*third:
            r = first*second*third
    for j in range(i+1,m): # 남은 부분을 세로로 절단
        second =getArea(0,n-1,i+1,j)
        third = tot-first-second
        if r< first*second*third:
            r = first*second*third

    
    
print(r)