from collections import defaultdict,deque

def solution(begin, target, words):
    answer=0
    d= defaultdict(int)
    q= deque()
    q.append(begin)
    d[begin]=1
    while q:
        print(q)
        now = q.popleft()
        if now == target:
            return d[now]-1
        for i in range(len(words)): 
            cnt=0
            for x,y in zip(now,words[i]):
                if x!=y:
                    cnt+=1
            if cnt==1 and d[words[i]]==0:
                d[words[i]] = d[now]+1
                q.append(words[i])
    return 0
begin=	"hit"	
target = "cog"
words=["hot", "dot", "dog", "lot", "log", "cog"]

solution(begin, target, words)