import re
s = '1220201abbd22dcd1004'
m = re.search('a.{0,10}c', s) # a.c와 일치하는 문자열을 찾는다. 
print(m)
if m!=None:
    print("일치")
    print(s)
else:
    print("불일치")

def makeKnumber(num, k):
    temp = ''
    while num:
        temp += str(num%k)
        num = num//k
    print(temp)
