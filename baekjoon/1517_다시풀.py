import sys
sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\baekjoon\\input.txt","rt")
n=int(input())

arr = list(map(int, sys.stdin.readline().split()))


def mergesort(lt,rt):
    global cnt
    if lt < rt :
        mid = (lt+rt)//2
        mergesort(lt,mid)
        mergesort(mid+1,rt)
        s1 = lt
        s2 = mid+1
        temp=[]
        while s1 <= mid and s2<=rt:
            if arr[s1]<= arr[s2]:
                temp.append(arr[s1])
                s1+=1
            else:
                temp.append(arr[s2])
                cnt += mid+1 -s1
                s2+=1
        if s1<=mid:
            temp = temp + arr[s1:mid+1]
        if s2<=rt :
            temp = temp + arr[s2:rt+1]
        for i in range(len(temp)):
            arr[lt + i] = temp[i]
cnt=0
mergesort(0,len(arr)-1)
print(cnt)