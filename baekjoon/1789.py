import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

n = int(input())

ans = 0
for i in range(4294967295):
    if n>=(i*(i+1))//2:
        continue
    else:
        ans =i
        break

print(ans-1)
