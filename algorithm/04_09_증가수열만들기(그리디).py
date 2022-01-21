import sys




#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")

n =  int(input())

a = list((map(int,input().split())))


last =0
lt =0
rt =n-1

str=''
while lt<rt:
    l=[]
    if a[lt] > last:
        l.append((a[lt], 'L'))
    if a[rt] > last:
        l.append((a[rt], 'R'))
    l.sort()
    if len(l)==0:
        break
    else:
        last = l[0][0]
        if l[0][1] =='L':
            lt+=1
            str+='L'
        else:
            rt-=1
            str+='R'
    

print(len(str))
print(str)


