import sys
import heapq
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n = int(sys.stdin.readline())
front = []
back = []

for i in range(n):
    num = int(sys.stdin.readline())
    if i==0:
        heapq.heappush(front,(-1)*num)
    elif i == 1:
        if -1*front[0]>num:
            heapq.heappush(back,front[0]*(-1))
            heapq.heapreplace(front,-1*num)
        else:
            heapq.heappush(back,num)
    else:
        if back[0]<num:
            heapq.heappush(front,back[0]*(-1))
            heapq.heapreplace(back,num)
        else:
            heapq.heappush(front,num*(-1))
    if len(front)-len(back)>1:
        tmp = heapq.heappop(front)
        heapq.heappush(back,tmp*(-1))
    print(front[0]*(-1))