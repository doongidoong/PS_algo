import sys
sys.stdin = open("C:\\Users\\wlgns\\pythonprogramming\\baekjoon\\input.txt","r")


T = int(input())
for i in range(T):
    n = input()
    temp = ''
    lenN = len(n)
    dp = [0 for i in range(10)] 
    if lenN == 1:
        for k in range(1,int(n)+1):
            dp[k] = 1
    else: 
        for i in range(lenN):
            num = int(n[0])
            if i == 0 :
                for j in range(1,num):
                    dp[j] +=10** (lenN-1)
                temp += str(num)
                n = n[1::]
                dp[num]+=int(n)+1
            else:
                if int(temp) != 0:
                    dp[0] +=(int(temp)-1)*10** (lenN-i-1)
                for k in range(1,10):
                    dp[k] +=(int(temp))*10** (lenN-i-1)
                for j in range(num):
                    dp[j] +=(1)*10** (lenN-i-1)
                temp += str(num)
                n = n[1::]
                if n :
                    dp[num]+=int(n)+1
                else:
                    dp[num]+=1
            print(dp)
    for i in dp:
        print(i,end=' ')
    print()

