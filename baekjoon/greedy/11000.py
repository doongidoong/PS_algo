import sys
import heapq
#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n=int( sys.stdin.readline())

lecture = sorted(tuple(map(int,  sys.stdin.readline().split())) for _ in range(n))  
endlist =[]
for s,e in lecture:
    if endlist and endlist[0]<=s:
        heapq.heapreplace(endlist,e)
    else:
        heapq.heappush(endlist,e)
print(len(endlist))