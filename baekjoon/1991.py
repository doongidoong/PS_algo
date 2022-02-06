import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n = int(input())

def DFS(v):
    if v != '.':
        print(v,end='')
        DFS(d[v][0])
        DFS(d[v][1])
        
def DFS2(v):
    if v != '.':
        DFS2(d[v][0])
        print(v,end='')
        DFS2(d[v][1])
        
def DFS3(v):
    if v != '.':
        DFS3(d.get(v)[0])
        DFS3(d.get(v)[1])
        print(v,end='')
        
d = {}

for i in range(n):
    root, left, right = sys.stdin.readline().strip().split()
    if i==0:
        top = root
    d[root] = [left, right]

DFS(top)
print()
DFS2(top)
print()
DFS3(top)