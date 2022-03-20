def solution(name):
    if set(name) == {'A'}:
        return 0

    answer = float('inf')
    for i in range(len(name) // 2): # 반 이상 움직일 필요 없음
        left_moved = name[-i:]+name[:-i] # 왼쪽으로 봄, i가 증가할 때마다 시작점이 왼쪽으로 한칸
        right_moved = name[i:]+name[:i] # 오른족으로 봄, i가 증까할때마다 시작점이 오른쪽으로 한칸
        print(left_moved,right_moved)
        for n in [left_moved, right_moved[0]+right_moved[:0:-1]]:
            while n and n[-1] == 'A':
                n = n[:-1]
            print(n)
            row_move = i + len(n)-1
            col_move = 0
            for c in map(ord, n):
                col_move += min(c - 65, 91 - c)

            answer = min(answer, row_move + col_move)

    return answer

name = "JEROEN"
print(solution(name))