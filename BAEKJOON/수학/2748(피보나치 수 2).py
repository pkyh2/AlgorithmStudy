n = int(input())

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif num == 2:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)

print(fibonacci(n))

# 시간 초과
# 동적 프로그래밍으로 풀어야 한다.
