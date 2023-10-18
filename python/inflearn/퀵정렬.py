#전위순회 먼저 호출 후 자기일을 해라
def  Qsort(lt,rt):
    if lt<rt:
        pos =lt
        pivot =rt
        for i in range(lt,rt):
            if arr[pivot]>arr[i]:
                arr[pos], arr[i]= arr[i], arr[pos]
                pos+=1
        arr[pos],arr[pivot] = arr[pivot],arr[pos]  
        Qsort(lt,pos-1)
        #  pos를 빼는 이유는 제 자리를 찾았기 때문
        Qsort(pos+1,rt)






if __name__ == "__main__" :
    arr = [45,21,23,36,15,67,11,60,20,33]
    print('before sort', arr)
    Qsort(0,9)
    print('after sort',arr)
    