def toKnumber(n, k): 
    ret = ""
    while n > 0:
        ret += str(n % k)
        n = n //  k
    return ''.join(reversed(ret))