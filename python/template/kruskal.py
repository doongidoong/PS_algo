import heapq
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
