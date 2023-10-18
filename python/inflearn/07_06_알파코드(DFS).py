
import sys

sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")

# 내풀이
n = input()

def dfs(numstr,s):
    global cnt
    if numstr != n[:len(numstr)]:
        return
    if len(numstr) >= len(n):
        if numstr==n:
            cnt+=1
            print(s)
        return
    else:
        for i in range(1,27):
            dfs(str(numstr)+str(i) , s+chr(i+64))
a=''
b= ''
cnt =0
dfs(a,b)
print(cnt)

"""

# 강의풀이
def DFS(L,P):
    global cnt
    if L==n:
        cnt+=1
        for j in range(P):
            print(chr(res[j]+64) ,end ='')
        print()

    else:
        for i in range(1,27):
            if code[L]==i :
                res[P] =i
                DFS(L+1,P+1)
            elif i >=10 and code[L] == i//10 and code[L+1] == i%10:
                res[P] = i
                DFS(L+2,P+1)


if __name__ == '__main__':
    code = list(map(int, input()))
    n = len(code) # 정착점
    code.insert(n,-1) #맨 마지막이 1이나 2일 경우 뒷자리까지 확인해야함, 인덱스 에러 방지
    res =[0]*(n+3)
    cnt =0
    DFS(0,0)
    print(cnt)
    



"""
