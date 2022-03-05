# 피보나치 함수
def fibonacci(num):
    global cnt_0, cnt_1
    if num == 0:
        cnt_0 += 1
        return 0
    elif num == 1:
        cnt_1 += 1
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    cnt_0, cnt_1 = 0, 0
    fibonacci(N)
    print('{} {}'.format(cnt_0, cnt_1))
# 시간초과

# 캐싱 사용
def fib_memo(n, cache): # num과 dict를 매개변수로
    global cnt_0, cnt_1
    if n < 3:
        cache[n] = 1
        return 1

    # 캐시에 n번째 피보나치가 있으면 바로 리턴
    if n in cache:
        return cache[n]

    # n번째 피보나치 수를 계산하지 않았으면
    # 계산 후 cache에 저장
    cache[n] = fib_memo(n-1, cache) + fib_memo(n-2, cache)
    print(cache)
    return cache[n]

def fib(n):
    fib_cache = {}
    return fib_memo(n, fib_cache)

T = int(input())
for _ in range(T):
    N = int(input())
    cnt_0, cnt_1 = 0, 0

    fib(N)
    # print('{} {}'.format(cnt_0, cnt_1))

# 복습!
# 40개를 미리 만들어 놓기
import sys
input = sys.stdin.readline

cache = {0:[1,0], 1:[0,1]}
for i in range(2, 41):
    cache[i] = [cache[i-2][j] + cache[i-1][j] for j in range(2)]

T = int(input())
for _ in range(T):
    N = int(input())
    print(' '.join(map(str, cache[N])))

# 30860 72