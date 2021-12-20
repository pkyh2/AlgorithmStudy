# 소트인사이드

# 풀이1
import sys

N = int(sys.stdin.readline())

numbers = []

while N:
    numbers.append(N % 10)
    N //= 10
numbers.sort(reverse=True)
for i in numbers:
    print(i, end='')

# 29200 68