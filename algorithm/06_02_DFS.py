import sys
#sys.stdin = open("C:\\Users\\82103\\pythonprogramming\\algorithm\\input.txt","r")

def dfs(v):
    if v>7:
        return 
    else:
        print(v, end=' ') # 전위순회 본연의 일 먼저함. 보통 전위순회 방식을 주로 씀
        dfs(2*v)
        #print(v, end=' ') #중위순회 왼쪽 자식이 먼저 처리되고 본연의 일을함
        dfs(2*v+1)
        #print(v, end=' ') #후위순회 병합정렬에 사용함
        

if __name__== "__main__":
    dfs(1)