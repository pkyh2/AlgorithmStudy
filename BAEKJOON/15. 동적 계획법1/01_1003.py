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

# memoization(재귀 사용)
# 이전에 계산한 값을 메모리에 저장
# 캐싱 사용
def fib_memo(n, cache): # num과 dict를 매개변수로
    if n < 3:
        return 1

    # 캐시에 n번째 피보나치가 있으면 바로 리턴
    if n in cache:
        return cache[n]

    # n번째 피보나치 수를 계산하지 않았으면
    # 계산 후 cache에 저장
    cache[n] = fib_memo(n-1, cache) + fib_memo(n-2, cache)
    return cache[n]

def fib(n):
    fib_cache = {}
    return fib_memo(n, fib_cache)

print(fib(N))


# tabulation(정답)
# 40개를 미리 만들어 놓기
import sys
input = sys.stdin.readline

# 0과 1의 출현 횟수가 fib의 방식이랑 동일하게 나타난다.
# 캐시에 다음 값을 앞의 값을 이용해서 계산 후 추가
cache = {0:[1,0], 1:[0,1]} # 1,1 1,2 2,3 3,5
for i in range(2, 41):
    cache[i] = [cache[i-2][j] + cache[i-1][j] for j in range(2)]

T = int(input())
for _ in range(T):
    N = int(input())
    print(' '.join(map(str, cache[N])))

# 30860 72


# list를 활용한 캐싱
def fib_list(num):
    fib_table = [0, 1, 1]

    for i in range(3, num+1):
        fib_table.append(fib_table[i-1] + fib_table[i-2])
    
    return fib_table[num]

fib_list(10)

# dict를 활용한 캐싱
def fib_dict(num):
    fib_cache = {1:1, 2:1} # 3:2

    for i in range(3, num+1):
        fib_cache[i] = fib_cache[i-1] + fib_cache[i-2]

    return fib_cache[num]

fib_dict(10)