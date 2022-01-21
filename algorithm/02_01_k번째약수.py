import sys
#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")
n,k = map(int, input().split())
cnt =0

for i in range(1,n+1):
    if n% i ==0:
        cnt +=1
    if cnt%k ==0:
        print(i)
        break
else: #정상적으로 끝나면 else 실행
    print(-1)
