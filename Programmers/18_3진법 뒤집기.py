def solution(n):
    answer = 0
    ternary = []
    while n > 0:
        ternary.append(n % 3)
        n //= 3
    ternary = ''.join(map(str, ternary))
    for i in range(len(ternary)):
        answer += int(ternary[len(ternary)-i-1]) * (3**i)
    return answer

n = 45
print(solution(n))
n = 125
print(solution(n))

# 풀이중...