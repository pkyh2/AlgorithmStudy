import sys
from itertools import permutations
input = sys.stdin.readline

T = int(input())

N = list(map(int, input().split()))
op = list(map(int, input().split()))
oper = []

# 연산자 추출
for i in range(len(op)):
    if op[i] != 0:
        for j in range(op[i]):
            if i == 0: oper.append('+')
            elif i == 1: oper.append('-')
            elif i == 2: oper.append('*')
            elif i == 3: oper.append('//')

# 사칙연산 순열(순서x) set으로 중복 연산을 제거
oper = list(set(permutations(oper,len(oper))))

# 사칙연산 만들기
ans = []
for i in oper:
    result = N[0]   # 1번째 숫자 입력
    # 다음 숫자로 넘어가면서 앞에 해당 연산자에 따라 연산
    for j in range(len(N)-1):   # 연산자 개수
        if i[j] == '+':
            result += N[j+1]
        elif i[j] == '-':
            result -= N[j+1]
        elif i[j] == '*':
            result *= N[j+1]
        else:
            # 음수로 몫 연산을 하면 양수로 몫 연산을 하고 음수로 바꾼다.
            if result // N[j+1] < 0:
                result = -(-result//N[j+1])
            else:
                result //= N[j+1]
    ans.append(result)

print(max(ans))
print(min(ans))
# 35980 612