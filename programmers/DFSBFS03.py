from cmath import inf
from collections import defaultdict

check = defaultdict(int)
answer = inf
def solution(begin, target, words):
    global answer, check
    check[begin]=1
    DFS(0,begin,words,target)
    if answer ==inf:
        answer=0
    return answer
def DFS(L,now,words,target):
    global answer
    if L ==len(words):
        return
    if now == target and answer > L:
        answer = L
        return answer
    for j in range(len(words)):
        cnt=0
        if check[words[j]]==0:
            for k in range(len(now)):
                if now[k]!=words[j][k]:
                    cnt+=1
        if cnt==1:
            check[words[j]] = 1 
            DFS(L+1,words[j],words,target)
            check[words[j]] = 0
begin=	"hit"	
target = "cog"
words=["hot", "dot", "dog", "lot", "log", "cog"]

solution(begin, target, words)