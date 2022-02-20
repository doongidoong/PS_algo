import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

st = input()
temp=''
num=[]
ans=0
# 1-1+1+1+1+1+1
# 1-(1+1)-(1+1)-1-1
target=-1
ind = 1
for i in st:
    if i == '+':
        ind+=1
        num.append(int(temp))
        temp=''
    elif i =='-':
        if target<0:
            target =ind
        ind+=1 
        num.append(int(temp))
        temp=''
    else:
        temp = temp+i
num.append(int(temp))
if target==-1:
    print(sum(num))
else:
    print(sum(num[:target])- sum(num[target:]))
