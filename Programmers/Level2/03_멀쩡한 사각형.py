# Level2

def gcd(w, h):
    a, b = max([w, h]), min([w, h])
    while(True):
        r = a%b
        if r == 0:
            return b
        a = b
        b = r

def solution(w, h):
    answer = w*h - (w+h - gcd(w, h))
    return answer