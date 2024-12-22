# 골드바흐의 추측

'''
2보다 큰 모든 짝수는 두 소수의 합을 표현하는게 골드바흐의 파티션 ex) 4 = 2 + 2, 12 = 5 + 7
파티션이 여러가지 인 경우는 두 소수의 차이가 가장 작은 것을 출력
'''

# 풀이1 (제곱근)
# 입력한 수의 절반에 가까운 작은 소수와 그 다음소수의 합
# ex) 30 15와 가까운 작은 소수 = 13, 그 다음 소수 17
# ex) 100 절반 50, 작은 소수 = 47 그 다음 소수 53
# 예외! 4 6 10 14 같은 동일한 소수의 덧셈

import time
start = time.time()

T = int(input())

def primeNumChecker(num):
    sieve = [True] * num
    m = int(num**0.5)

    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, num, i):
                sieve[j] = False

    return [i for i in range(2, num) if sieve[i] == True]

for _ in range(T):
    n = int(input())

    half_n = n//2

    if n == 4:
        print(2, 2, sep=' ')

    primeNum = primeNumChecker(half_n+1)

    for i in range(1, len(primeNum)):
        ans1 = primeNum[len(primeNum) - i]  #[1 3 5 7 11]  len(pr) - 1 = 4
        ans2 = n - ans1
        confirm = primeNumChecker(ans2+1)
        if ans2 not in confirm:
            continue
        else:
            print(ans1, ans2, sep=' ')
            break

end = time.time()
print(f"{end - start:.5f} sec")

# 시간 초과...

# 풀이2
'''
T = int(input())

def primeNumPrinter(num):
    numbers = set(range(2, num+1))

    for i in range(2, num+1):
        if i in numbers:
            numbers -= set(range(2*i, num+1, i))

    return [i for i in numbers]

def primeNumChecker(num):
    numbers = set(range(2, num+1))

    for i in range(2, num+1):
        if i in numbers:
            numbers -= set(range(2*i, num+1, i))

    if num in numbers:
        return True
    else:
        return False

for _ in range(T):
    n = int(input())

    half_n = n//2

    primeNum = primeNumPrinter(half_n+1)
    primeNum = primeNum[::-1]

    for i in primeNum:
        ans1 = i
        ans2 = n - ans1
        if primeNumChecker(ans2) == False:
            continue
        else:
            print(ans1, ans2, sep=' ')
            break
'''
# 시간초과...

# 풀이3 차집합
# 1. 10000까지의 범위니까 set으로 전체에서 짝수는 있을 수 없으니까 소수로만 이루워진 집합 생성
# 2. 홀수의 배수들을 제거
# 3. 입력받은 수의 절반보다 작은 가장 가까운 소수를 찾는다.
# 4. 입력받은 수에서 그 소수를 뺀 수가 위부분 소수에 있는지 확인하고 있으면 출력

import time
start = time.time()

# 2 ~ 10000까지 소수 list 생성
import math
numbers = {i for i in range(2, 10001) if i == 2 or i % 2 == 1}      # 2와 홀수 set
for i in range(3, int(math.sqrt(10000))+1, 2):                      # 3에서 홀수에 해당하는 수 반복
    numbers -= {j for j in range(2*i, 10001, i) if j in numbers}    # 홀수의 배수로 이루어진 집합을 빼준다.
# numbers에는 10000까지 소수가 있다.

T = int(input())
for _ in range(T):
    even = int(input())
    half = even // 2

    for x in range(half, 1, -1):
        if (even - x) in numbers and (x in numbers): # 88 -> 47, 41(o) 
            print(x, even - x)
            break

end = time.time()
print(f"{end - start:.5f} sec")