#순열이 아닌 조합으로 풀어야 한다.
import sys
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\baekjoon\\input.txt","rt")
n=int(sys.stdin.readline())

numbers = [1, 5, 10, 50]
res = [0 for _ in range(100001)]
count =0
def DFS(L,t,s):
    global count 
    if L==n:
        if res[t]==0:
            count+=1
            res[t]=1
        return
    for i in range(s,4):
        DFS(L+1,t+numbers[i],i)

DFS(0,0,0)
print(count)