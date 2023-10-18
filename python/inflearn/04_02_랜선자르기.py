import sys
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\algorithm\\input.txt","r")


def solution(k,n,wires):
    lt =  0
    rt  = max(wires)
    answer = 0
    while lt <= rt:
        mid = (lt+rt) //2
        cnt = count(wires, mid)
        if cnt < n :        
            rt  = mid -1
        else:
            lt = mid + 1
            answer = mid
    print(answer)
    return


def count(wires ,length) :
    cnt = 0
    for wire in wires:
        cnt += wire//length
    return cnt
k , n = map(int,input().split())
wires = []
for i in range(k):
    wire = int(input())
    wires.append(wire)

solution(k,n,wires)