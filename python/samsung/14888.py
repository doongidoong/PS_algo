import sys

sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\samsung\\input.txt","r")
n = int(input())
numbers = list(map(int, input().split()))
a,b,c,d = map(int, input().split())

temp = set()
def DFS(L,num, a,b,c,d):
    if L== n-1:
        temp.add(num)
        return
    if b>=1 :
        DFS(L+1,num-numbers[L+1],a,b-1,c,d)
    if c>=1 :
        DFS(L+1,num*numbers[L+1],a,b,c-1,d)
    if d>=1 :
        if num < 0:
            DFS(L+1,-(-num//numbers[L+1]),a,b,c,d-1)
        else:
            DFS(L+1,num//numbers[L+1],a,b,c,d-1)    
    if a>=1 :
        DFS(L+1,num+numbers[L+1],a-1,b,c,d)    
    
        
DFS(0,numbers[0],a,b,c,d)
print(max(temp))
print(min(temp))