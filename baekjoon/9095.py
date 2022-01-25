import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n = int(input())
dy =[0,1,2,4]
for _ in range(n):
    k = int(input())
    if k>len(dy)-1:
        for i in range(len(dy),k+1):
            dy.append(dy[i-1]+dy[i-2]+dy[i-3])
    print(dy[k])