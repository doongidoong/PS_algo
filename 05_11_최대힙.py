
import sys
import heapq as hq
sys.stdin = open("input.txt","rt")
# 파이썬의 heapq는 최소힙을 가정함 따라서 최대힙은 코드의 수정이 약간 필요
# 그건 바로 음수를 취해주는 것 음수를 취해주면 가장 큰수가 가장 작아지고  
# 가장 작은 수가 가장 크게 됨. 출력할 때 다시 -1을 곱해서 출력하면 됨
a = [] 
temp=[]
while True:
    n = int(input())
    if n ==-1:
        break
    if n==0:
        if len(a)==0:
            print(-1)
        else:
           print(hq.heappop(a)*-1) 
    else:
        hq.heappush(a , -1*n)