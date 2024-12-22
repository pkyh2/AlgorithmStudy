# 소수 구하기

'''
M이상 N이하의 소수를 모두 출력하시오.
'''

# 풀이 1 (제곱근)
'''
import time
start = time.time()

import math

M, N = map(int, input().split())
numbers = list(range(M, N+1))

for i in numbers:
    cnt = 0
    if i > 1:
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0:
                cnt += 1
        if cnt == 0:
            print(i)

end = time.time()
print(f"{end - start:.5f} sec")
'''
# 시간초과...

# 풀이 2 (에라토스테네스의 체)
import time
start  = time.time()

M, N = map(int, input().split())

def primeNumChecker(num):
    sieve = [True] * num        # num개의 True배열 생성 (소수라고 가정)     ex) [True, True, True ... True] num개

    m = int(num**0.5)           # num의 제곱근 대입
    for i in range(2, m+1):     # num의 제곱근까지 반복
        if sieve[i] == True:    # i가 소수일때
            for j in range(i+i, num, i): # i이후의 i의 배수들을 False처리
                sieve[j] = False
    
    return [i for i in range(2, num) if sieve[i] == True]
    # list1 = [1, 2, 2, 3, 4, 5] / list1 = [i for i in range(1, 5)]

result = primeNumChecker(N+1)
for i in result:
    if i >= M:
        print(i)

end = time.time()
print(f"{end - start:.5f} sec")