import sys
#sys.stdin = open("input.txt","rt")
str1 = input()
str2 = input()
d1={}
check =0
for i in str1:
    d1[i] = d1.get(i,0) +1 # 없으면 0값을 리턴
for i in str2:
    if d1.get(i,0) == 0:
        check=1
    else:
        d1[i] = d1.get(i,0) -1
    

for x in str1:
    if d1.get(x) !=0:
        print("NO")
        break
else:
    if check==1:
        print("NO")
    else:
        print("YES")