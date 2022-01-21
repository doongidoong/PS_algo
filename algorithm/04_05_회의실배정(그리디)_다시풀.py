import sys
#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")

n= int(input())
meeting = []
for i in range(n):
    s,e = map(int, input().split())
    meeting.append((s,e))


meeting.sort(key = lambda x : (x[1],x[0])) # 튜플은 앞의 자료에 의해 정렬함

et =0 # 현재 끝나는 시간
cnt = 0

for start,end in meeting:
    if start>=et:
        et = end
        cnt +=1

print(cnt)
