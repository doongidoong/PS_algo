import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n=int(input())
L =[]
for i in range(n):
    d,a,b,c = sys.stdin.readline().split()
    temp = list(map(int, (a,b,c)))
    temp.append(d)
    L.append(temp)


L.sort(key= lambda x: (-1*x[0],x[1],-1*x[2],x[3]))
for i in L:
    print(i[-1])