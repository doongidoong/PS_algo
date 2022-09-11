import re
from itertools import permutations
def solution(user_id, banned_id):
    ban = ' '.join(banned_id).replace('*','.') # 1개를 뜻하는 .로 replace
    print(ban)
    answer = set()
    for i in permutations(user_id, len(banned_id)):
        if re.fullmatch(ban, ' '.join(i)):
            answer.add(''.join(sorted(i)))
    return len(answer)

solution(["frodo", "fradi", "crodo", "abc123", "frodoc"] , ["fr*d*", "abc1**"]	)