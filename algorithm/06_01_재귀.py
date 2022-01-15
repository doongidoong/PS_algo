import sys
sys.stdin = open("input.txt","rt")
n = int(input())


def dfs(x):
    if x==0:
        return
    else:
        dfs(x//2)
        print(x%2, end= '')


dfs(n)