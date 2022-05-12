def solution(n):
    answer = 0
    ternary = []
    while n > 0:
        ternary.append(n % 3)
        n //= 3
    ternary = int(''.join(map(str, ternary)))
    answer = int(ternary, 3) 
    return answer

n = 45
print(solution(n))
n = 125
print(solution(n))

# 풀이중...