def solution(sales, links):
    answer = 0    
    v = len(sales)
    parent = [0] * (v + 1) # 부모 테이블 초기화하기
    # 부모 테이블상에서, 부모를 자기 자신으로 초기화
    for i in range(1, v + 1):
        parent[i] = i
    # Union 연산을 각각 수행
    for a,b in links:
        union(parent,a, b)
    print(parent)
    return answer

# 특정 원소가 속한 집합을 찾기
def find(parent,x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find(parent,parent[x])
    return x

# 두 원소가 속한 집합을 합치기
def union(parent,a, b):
    a = find(parent,a)
    b = find(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
