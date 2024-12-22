# 배르트랑 공준

'''
n과 2n 사이의 소수의 개수를 구하시오.
'''

# 풀이1 (에라토스테네스의 체!)

def primeNumChecker(num):
    sieve = [True] * num        # num개의 True 리스트 생성

    m = int(num**0.5)           # sqrt(num)까지만 반복
    for i in range(2, m + 1):    # 2인덱스 부터
        if sieve[i] == True:
            for j in range(i+i, num, i):
                sieve[j] = False

    return [i for i in range(2, num) if sieve[i] == True]

import time
start = time.time()

while True:
    n = int(input())
    nn = n*2

    if n == 0:
        break
    else:
        primeNumbers = primeNumChecker(nn + 1)
        result = []

        for i in primeNumbers:
            if i > n:
                result.append(i)

        print(len(result))

end = time.time()
print(f"{end - start:.5f} sec")