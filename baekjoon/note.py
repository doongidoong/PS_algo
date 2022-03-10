l = list(map(int,input().split()))
temp= 0
for i in l:
    temp+=i*i

print(temp%(10))