import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

dy=[0 for _ in range(50001)]
s = input()
temp=''
if len(s)==0:
    print(0)
    sys.exit(0)
dy[0]=1
for i in range(len(s)):
    temp += s[i]
    if int(s[i])>0:
        dy[i+1] += dy[i]
    if 10<=int(temp) <= 26 :
        dy[i+1] += dy[i-1]
    temp = s[i]
print(dy)
print(dy[len(s)]%1000000)