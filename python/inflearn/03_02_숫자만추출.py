import sys


#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")

s = input()

num = 0
for i in s:
    if ord(i)>= 48 and ord(i)<=57 : #i.isdecimal()과 같은 효과
        num *= 10
        num += int(i) 
count =0
for i in range(1,num+1):
    if num%i ==0:
        count+=1
print(num)
print(count)
