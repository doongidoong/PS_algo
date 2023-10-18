import sys

sys.setrecursionlimit(10**6) # 재귀의 타임 리미트 설정 보통 10 6제곱 정도

preOrdArr = []
postOrdArr = []
idx  = {}
def solution(nodeinfo):
    answer = []
    depthArr = sorted(nodeinfo, key = lambda x :(-x[1],x[0]) )
    for i in range(len(nodeinfo)):
        idx[nodeinfo[i][0]] = i+1
    preOrder(depthArr)
    answer.append(preOrdArr)

    postOrder(depthArr)
    answer.append(postOrdArr)

    return answer
def preOrder(arr):
    global preOrdArr
    parent = arr[0]
    leftChild = []
    rightChild =[]
    for point in arr:
        if point[0] < parent[0]:
            leftChild.append(point)
        elif point[0] > parent[0] :
            rightChild.append(point)
    preOrdArr.append(idx[parent[0]])
    if leftChild:
        preOrder(leftChild)
    if rightChild:
        preOrder(rightChild)



def postOrder(arr):
    global postOrdArr
    parent = arr[0]
    leftChild = []
    rightChild =[]
    for point in arr:
        if point[0] < parent[0]:
            leftChild.append(point)
        elif point[0] > parent[0] :
            rightChild.append(point)
    if leftChild:
        postOrder(leftChild)
    if rightChild:
        postOrder(rightChild)
    postOrdArr.append(idx[parent[0]])


solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])