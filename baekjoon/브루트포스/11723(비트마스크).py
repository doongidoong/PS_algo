import sys

sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\pythonprogramming\\baekjoon\\input.txt","rt")

input = sys.stdin.readline


n= int(input())

bit = 0
for i in range(n):
    command = input().rstrip()
    if command=='all':
        bit = (1<<20)-1
    elif command == "empty":
        bit = 0
    else:
        com, num = command.split()
        num = int(num)-1
        if com == 'add':
            bit = bit|(1<<num)
        elif com == 'remove':
            bit = bit&~(1<<num)
        elif com == 'check':
            if bit&(1<<num):
                print(1)
            else:
                print(0)
        elif com == 'toggle':
            bit = bit^(1<<num)
