import sys
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")

N, S = map(int, input().split())
L = list(map(int, input().split()))

answer = 0

for i in range(1,1<<N):
    temp =0
    for j in range(N):
        if i&(1<<j):
            temp += L[j]
    if temp == S:
        answer+=1

print(answer)