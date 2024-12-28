# 분해합
'''
자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다.
ex) 245의 분해합은 245 + 2 + 4 + 5 = 256 -> 245는 256의 생성자
자연수 N(256)이 주어졌을 때, N의 가장 작은 생성자(245)를 구하시오.
'''

# 풀이1
# N을 입력받고
# 1부터 반복하여 모든 수를 분해합 해본다. 분해합의 결과가 N값이 되는 순간 종료
# while i <= N:

# T = int(input())
# for _ in range(T):
import sys
N = int(sys.stdin.readline())
i = 1
while True:
    temp = i
    if i < 10:
        digit_sum = i + i
        if digit_sum == N:      # 최대가 18
            print(i)
            break
        elif digit_sum > 18:
            print(0)
            break
    else:
        digit_sum = i           # 245대입 91
        while temp > 0:         # 첫 temp는 == i 다 245         
            one = temp % 10     # 5, 4
            digit_sum += one       # 245 + 5 + 4
            temp //= 10         # temp = 24
        if digit_sum == N:
            print(i)
            break
        elif i > N:
            print(0)
            break
    i += 1

#29200KB 1480ms