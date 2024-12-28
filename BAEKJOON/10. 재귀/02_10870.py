# 피보나치 수 5

import sys
N = int(sys.stdin.readline())

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(N))

# 29200KB 80ms