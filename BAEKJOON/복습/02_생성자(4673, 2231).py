# 4673 셀프넘버
# 1 ~ 10000까지 생성
notSelfNum = list(range(1, 10001))

def check(num):
    selfNum = num
    while num > 0:
        selfNum += num % 10
        num //= 10

    return selfNum

for i in range(1, 10001):
    selfNum = check(i)
    if selfNum in notSelfNum:
        notSelfNum.remove(selfNum)

for i in range(len(notSelfNum)):
    print(notSelfNum[i])
# 30860 228

# set 사용
notSelfNum = set(range(1, 10001))

def check(num):
    selfNum = num
    while num > 0:
        selfNum += num % 10
        num //= 10

    return selfNum

for i in range(1, 10001):
    selfNum = check(i)
    if selfNum in notSelfNum:
        notSelfNum.remove(selfNum)

notSelfNum = sorted(list(notSelfNum))
for i in range(len(notSelfNum)):
    print(notSelfNum[i])
# 31372 76


# 2231 분해합
import sys
input = sys.stdin.readline

def check(num):
    selfNum = num
    while num > 0:
        selfNum += num % 10
        num //= 10

    return selfNum

N = int(input())
flag = 1
i = 1
while i <= N:
    selfNum = check(i)
    if selfNum == N:
        print(i)
        flag = 0
        break
    i += 1

if flag == 1:
    print(0)
# 30860 892

# 자리 수로 계산(1부터 계산하지 않고)
# 분해합을 만들 수 있는 가장 작은 숫자부터 시작
import sys
input = sys.stdin.readline

def check(num):
    selfNum = num
    while num > 0:
        selfNum += num % 10
        num //= 10

    return selfNum

N = int(input())
flag = 1
# 입력받은 숫자의 최소 생성자는 자리수에 9를 곱한 값을 빼준 값부터 이다.
minimum = N - 9*len(str(N))
maximum = N - 1
while minimum <= maximum:
    selfNum = check(minimum)
    if selfNum == N:
        print(minimum)
        flag = 0
        break
    minimum += 1

if flag == 1:
    print(0)
# 30864 68