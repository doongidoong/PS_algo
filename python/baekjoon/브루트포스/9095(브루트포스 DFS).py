
import sys

def DFS(t):
    global answer
    if t>n:
        return
    if t==n:
        answer+=1
        return
    for i in range(1,4):
        DFS(t+i)

sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")
T = int(input())
for i in range(T):
    n = int(input())
    answer = 0
    DFS(0)
    print(answer)


        

