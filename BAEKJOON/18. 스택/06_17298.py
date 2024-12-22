# 오큰수

'''
크기가 N 인 수열
A(i) 에 대해서 오큰수 NGE(i)를 구하려한다.
A(i)의 오큰수는 오른쪽에 있으면서 A(i)보다 큰 수중 가장 왼쪽에 있는 수
그러한 수가 없으면 -1
'''

# 풀이1
# import sys
# input = sys.stdin.readline
# N = int(input())
# sequence = list(map(int, input().split()))
# NGE = []
# top = -1
# stack = [None for _ in range(N)]
# for i in sequence: #9 5 4 8
#     cnt = 0
#     top += 1
#     stack[top] = i
#     for j in sequence[top+1:]:
#         if stack[top] < j:
#             cnt += 1
#             NGE.append(j)
#             break
#     if cnt == 0:
#         NGE.append(-1)

# for i in NGE:
#     print(i, end=' ')
# 시간초과

# 풀이2 스택을 오른쪽부터 적용
# import sys
# input = sys.stdin.readline
# N = int(input())
# sequence = list(map(int, input().split()))
# NGE = []
# top = -1
# stack = [None for _ in range(N)]
# for i in sequence[::-1]:
#     cnt = 0
#     top += 1
#     stack[top] = i
#     for j in sequence[-(top+1):]:
#         if stack[top] < j:
#             cnt += 1
#             NGE.append(j)
#             break
#     if cnt == 0:
#         NGE.append(-1)

# for i in NGE[::-1]:
#     print(i, end=' ')

# ㅜㅜ시간초과

# 풀이3
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