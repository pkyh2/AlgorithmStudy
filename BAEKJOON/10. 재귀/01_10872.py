# 팩토리얼

import sys
N = int(sys.stdin.readline())
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(N))

# 29200KB 72ms