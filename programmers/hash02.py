def solution(phone_book):
    l = phone_book
    l.sort()
    lt= 0
    cur =1
    while cur<len(l):
        if l[cur].startswith(l[lt]):
            return False
        else:
            lt=cur
            cur += 1
    return True
                
phone_book= ["12","1234","567","88"]
phone_book.sort()
print(solution(phone_book))