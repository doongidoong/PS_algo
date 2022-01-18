import sys
from collections import deque
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")
n = int(input())  

board = [list(map(int, input().split())) for _ in range(n)]
Q = deque()
dx =[1,-1,0,0]
dy =[0,0,1,-1]
