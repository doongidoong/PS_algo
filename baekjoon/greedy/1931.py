import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

n = int(input())
a=[]
for i in range(n):
    s, e = map(int, input().split())
    a.append((s,e))

a.sort(key= lambda x : (x[1],x[0])) # 끝나는 시간 기준으로 정렬


pre_end = a[0][1] # 이전 회의가 끝나는 시간
cnt=1
for i in range(1,len(a)):
    if a[i][0]>=pre_end: # 전에 체크한 회의가 끝나는 시간이 시작하는 시간보다 빠르거나 같을 경우
        cnt+=1
        pre_end = a[i][1]

print(cnt)