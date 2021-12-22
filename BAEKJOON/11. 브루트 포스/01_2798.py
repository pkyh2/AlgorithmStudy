# 블랙잭
'''
N 장의 카드를 모두 보이도록 바닥에 놓는다.
딜러가 숫자 M을 크게 외친다.
N장 중 3장의 카드를 골라야 한다.
3장의 카드 합이 M을 넘지않는 최대한 가까운 수를 출력하시오.
'''

# 풀이1 for문
# 1, 2, 3
# 1, 2, 4
# 1, 2, 5 ...
import sys
N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

result = []

for i in range(len(cards)):
    for j in range(1, len(cards)):
        for k in range(2, len(cards)):
            if i < j < k:       # 핵심 키워드!
                cardsSum = cards[i]+cards[j]+cards[k]
                if cardsSum <= M:
                    result.append(cardsSum)

print(max(result))
#35316KB 208ms

# 풀이2 while문
import sys
N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

result = []

i = 0
while i < len(cards):
    j = i+1
    while j < len(cards):
        k = j+1
        while k < len(cards):
            cardsSum = cards[i]+cards[j]+cards[k]
            if cardsSum <= M:
                result.append(cardsSum)
            k += 1
        j += 1
    i += 1

print(max(result))
# 35316KB 144ms

## 시간 줄이는 법
# set함수 사용
import sys
N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

result = set()                  # 합계에 중복이 있을 수 있으니까

i = 0
while i < len(cards):
    j = i+1
    while j < len(cards):
        k = j+1
        while k < len(cards):
            if i < j < k:       #핵심 키워드!
                cardsSum = cards[i]+cards[j]+cards[k]
                if cardsSum <= M:
                    result.add(cardsSum)
            k += 1
        j += 1
    i += 1

print(max(result))