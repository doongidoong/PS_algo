import sys

sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

s= sys.stdin.readline().rstrip()

for i in range(len(s)):
    if 97<=ord(s[i])<=109:
        print(chr(ord(s[i])+13),end='')
    elif 110<=ord(s[i])<=122:
        print(chr(ord(s[i])-13),end='')
    elif 65<=ord(s[i])<=77:
        print(chr(ord(s[i])+13),end='')
    elif 78<=ord(s[i])<=90:     
        print(chr(ord(s[i])-13),end='')
    
    else:
        print(s[i],end='')
