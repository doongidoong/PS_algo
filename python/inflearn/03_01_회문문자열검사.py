import sys

#sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\algorithm\\input.txt","rt")

n = int(input())
for i in range(n):
    s = sys.stdin.readline().strip().lower()
    lt =0
    rt = len(s)-1
    flag = "YES"
    while lt<rt:
        a = s[lt]
        b = s[rt]
        if a!=b:
            flag= "NO"
            break
        lt +=1
        rt -=1
    print("#{} {}".format(i+1,flag))