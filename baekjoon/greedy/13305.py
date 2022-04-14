import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

n = int(input())

dis = list(map(int,input().split()))
city = list(map(int,input().split()))



price= 1000000000
ans =0
for i in range(len(city)-1):
    if city[i]<price:
        price=city[i]
    ans+=price*dis[i]

print(ans)