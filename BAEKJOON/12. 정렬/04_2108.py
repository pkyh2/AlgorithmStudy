# 통계학
# 풀이1 package
import sys
from collections import Counter

N = int(sys.stdin.readline())
numbers = []
for i in range(N):
    num = int(sys.stdin.readline())
    numbers.append(num)

numbers.sort()

mean = round(sum(numbers) / len(numbers))
median = numbers[len(numbers)//2]

mode = Counter(numbers).most_common(2)
if len(mode) > 1:
    if mode[0][1] == mode[1][1]:
        modeA = mode[1][0]
    else:
        modeA = mode[0][0]
else:
    modeA = mode[0][0]

print(mean)
print(median)
print(modeA)
print(max(numbers) - min(numbers))

# 52880KB 540ms

# 풀이2 dict
import sys
from collections import Counter

N = int(sys.stdin.readline())
numbers = []
for i in range(N):
    num = int(sys.stdin.readline())
    numbers.append(num)

numbers.sort()

mean = round(sum(numbers) / len(numbers))
median = numbers[len(numbers)//2]

mode = {}
for i in numbers:
    if i in mode:
        mode[i] = mode[i] + 1
    else:
        mode[i] = 1

modes = []
for k, v in mode.items():
    if v == max(mode.values()):
        modes.append(k)

print(mean)
print(median)
if len(modes) > 1:
    print(modes[1])
else:
    print(modes[0])
print(max(numbers) - min(numbers))

# pypy3 161668 616
# 52992 1716