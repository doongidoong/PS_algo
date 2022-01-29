import sys

sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")


while(1):
    try:
        s = input()
        temp = [0,0,0,0]
        for i in range(len(s)):
            if 48<=ord(s[i])<=57:
                temp[2]+=1
            elif s[i]==' ':
                temp[3]+=1
            elif 97<=ord(s[i])<=122:
                temp[0]+=1
            elif 65<=ord(s[i])<=90:
                temp[1]+=1
            else:
                continue
        for i in temp:
            print(i,end=' ')
        print()
    except EOFError:
        break
