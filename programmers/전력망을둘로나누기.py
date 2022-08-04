
parent=[]
def solution(n, wires):
    parent = [-1]*n
    for a,b in wires:
        union(a,b,parent)
    
def find(x,parent):
    if parent[x]< 0:
        return x
    parent[x] = find(x,parent)
    return parent[x]

def union(x, y,parent):
    x = find(x,parent) #x와 y의 루트노드를 찾아준다.
    y = find(y,parent)
    if x == y: #루드가 같다면 합칠 필요가 없으니 종료
        return
    if parent[x] < parent[y] :#x의 부모를 y로 만들어 합쳐주기
        parent[x] += parent[y]
        parent[y] =x
    else:
        parent[y] += parent[x]
        parent[x] =y
n= 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
solution(n,wires)