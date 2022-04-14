import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")

def get_dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

n=int(input())
spot = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    spot.append((a,b))


