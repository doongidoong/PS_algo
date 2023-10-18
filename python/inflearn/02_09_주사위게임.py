import sys

#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")

N = int(input())

money =[]

for i in range(N):
    L = list(map(int,input().split()))
    Lcount = [0]*7
    for i in L:
        Lcount[i] +=1
    if max(Lcount)==3:
        money.append(10000+ 1000*(Lcount.index(max(Lcount))))
    elif max(Lcount) ==2:
        money.append(1000+ 100*(Lcount.index(max(Lcount))))
    else:
        money.append(max(L)*100)

print(max(money))

