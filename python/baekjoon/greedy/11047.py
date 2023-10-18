import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

n, k = map(int, input().split())

coin = list(int(input()) for _ in range(n))

coin.sort(reverse=True)

res= 0
for i in coin:
    r = k//i
    k -= i*r
    res+=r

print(res) 