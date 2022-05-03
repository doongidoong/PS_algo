import sys
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")

n = int(input())
dy =[0]*(n+1)
dy[1]=0


for i in range(2,n+1):
    if i% 6 == 0 :
        dy[i] = min(dy[i-1],dy[i//2],dy[i//3])+1
    elif i%2 ==0:
        dy[i] = min(dy[i-1],dy[i//2])+1
    elif i%3 ==0:
        dy[i] = min(dy[i-1],dy[i//3])+1
    else:
        dy[i]= dy[i-1]+1

print(dy[-1])