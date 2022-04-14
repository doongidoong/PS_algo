def DFS(n):
    global s
    if n==0:
        return
    else:
        if n%-2<0:
            m = (n//-2)+1
            r = m*2+n
        else:
            m=n//-2
            r=n%(-2)
        DFS(m)
        s+=str(r)

n= int(input())
if n==0:
    print(0)
else:    
    s=''
    DFS(n)
    print(s)