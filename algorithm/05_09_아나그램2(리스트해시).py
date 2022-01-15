#딕셔너리를 쓰지 않고 직접 해싱하는방버

import sys
sys.stdin = open("input.txt","rt")
a = input()
b = input()

str1 = [0]*52 # 알파벳 대소문자 포함 개수가 52개
str2 = [0]*52
for x in a:
    if x.isupper():
        str1[ord(x)-65] += 1  #대문자 A는 65
    else: # 소문자는 97 // 32가 차이나지만 사실 알파벳은 26개 따라서 26부터 시작해야함
        str1[ord(x)-72] +=1

for x in b:
    if x.isupper():
        str2[ord(x)-65] += 1
    else: 
        str2[ord(x)-72] +=1

for i in range(52):
    if str1[i] != str2[i] :
        print("NO")
        break
else:
    print("YES")