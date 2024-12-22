# 2581 소수(제곱근)
import sys
import math
input = sys.stdin.readline

M = int(input())
N = int(input())

numbers = list(range(M, N+1))
primeNum = []
for num in numbers:
    cnt = 0
    if num > 1:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                cnt += 1
                break
        if cnt == 0 and num != 1:
            primeNum.append(num)

if len(primeNum) == 0:
    print(-1)
else:
    print(sum(primeNum))
    print(min(primeNum))

# 32972 88

# 1929 소수 구하기(에라토스테네스의 체)
import sys
input = sys.stdin.readline

M, N = map(int, input().split())

def primeNumChecker(num):
    sieve = [True] * num        # num개의 True원소 생성 (소수라고 가정)

    m = int(num**0.5)           # num의 제곱근까지만 반복
    for i in range(2, m+1):
        if sieve[i] == True:    # sieve[i]가 소수일때
            for j in range(i+i, num, i):    # 2이후의 num까지 2의 배수들을 False처리
                sieve[j] = False

    # 남은 2부터 True들만 return
    return [i for i in range(2, num) if sieve[i] == True]

result = primeNumChecker(N+1)
for i in result:
    if i >= M:
        print(i)

# 41204 284