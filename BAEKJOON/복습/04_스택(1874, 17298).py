# 1874 스택 수열
import sys
input = sys.stdin.readline

n = int(input())
stack = []
result = []
cnt, pointer= 1, 0
for _ in range(n):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        result.append('+')
        cnt += 1

    if num == stack[-1]:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        pointer = 1
        break

if pointer == 0:
    for i in result:
        print(i)
        
# 31296 220

# 17298 오큰수
import sys
input = sys.stdin.readline
N = int(input())
sequence = list(map(int, input().split()))
NGE = [-1] * N  # -1로 전부 초기화
stack = [0]

for i in range(len(sequence)):
    # 조건을 만족하면 NGE의 해당 인덱스에 sequence값을 넣어준다.
    while stack and sequence[stack[-1]] < sequence[i]:  # sequence[stack]
        NGE[stack.pop()] = sequence[i]
    # NGE를 구하지 못해도 index는 추가해줘야 한다.
    stack.append(i)

for i in NGE:
    print(i, end=' ')

# 152420 1464