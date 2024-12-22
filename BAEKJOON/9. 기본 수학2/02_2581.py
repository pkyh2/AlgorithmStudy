# 소수

'''
두 수가 주워졌을때 두 수를 포함하는 사이의 수들 중에서 소수를 골라 그들의 합과 그 들 중에서 최솟값을 찾아라
'''

# 풀이 1
# 1. 두 수를 입력받는다.
# 2. 두 수 사이의 수를 포함하는 list를 만든다.
# 3. list를 반복하면서 소수가 아니면 제거 해준다.
# 4. 합과 최솟값을 구한다.
'''
M = int(input())
N = int(input())
numbers = list(range(M, N+1))
prime_num = []

for num in numbers:
    not_prime_num = 0
    if num > 1:                     # num가 1보다 클때 2와 num-1 까지 반복
        for i in range(2, num):
            if num % i == 0:
                not_prime_num += 1
        if not_prime_num == 0:
            prime_num.append(num)

if len(prime_num) < 1:
    print(-1)
else:
    print(sum(prime_num))
    print(min(prime_num))
'''
# 시간초과... 시간 복잡도 O(N)

# 풀이 2
# 해당 숫자의 절반까지만 계산한다.
'''
M = int(input())
N = int(input())
numbers = list(range(M, N+1))
prime_num = []

for num in numbers:
    not_prime_num = 0
    if num > 1:                     # num가 1보다 클때 2와 num-1 까지 반복
        for i in range(2, int((num+1)/2)):
            if num % i == 0:
                not_prime_num += 1
        if not_prime_num == 0:
            prime_num.append(num)

if len(prime_num) < 1:
    print(-1)
else:
    print(sum(prime_num))
    print(min(prime_num))
    print(prime_num)
# 틀렸습니다.. 시간 복잡도 O(N)
'''
# 풀이 3
# 해당 숫자의 제곱근까지만 확인하는 방법!! 
import time
start = time.time()

import math

M = int(input())
N = int(input())
numbers = list(range(M, N+1))
prime_num = []

for num in numbers:                                 # 60부터 시작
    cnt = 0
    if num > 1:
        for i in range(2, int(math.sqrt(num))+1):   # 루트60까지
            if num % i == 0:
                cnt += 1
        if cnt == 0:
            prime_num.append(num)

if len(prime_num) < 1:
    print(-1)
else:
    print(sum(prime_num))
    print(min(prime_num))

end = time.time()
print(f"{end - start:.5f} sec")
# 3.85312 sec
# 제곱근으로 푸는법 다시 해보기(완료)


# 풀이 4
# 주어진 숫자까지 반복하는데 그 숫자를 한번도 방문한적 없다면 소수
# 그 수의 배수는 소수가 아니다
# 중간부터 시작하는 숫자는 풀이가 애매함