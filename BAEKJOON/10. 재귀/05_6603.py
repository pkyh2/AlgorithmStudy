# 로또

from itertools import combinations
import sys
input = sys.stdin.readline

while True:
    lotto = list(map(int, input().split()))
    if lotto.pop(0) == 0:
        break
    else:
        result = combinations(lotto, 6)
        for i in result:
            print(' '.join(map(str, i)))
    print()

# import sys
# input = sys.stdin.readline

# def dfs(start):
#     # 길이가 같아지면 1조합 출력
#     if len(s) == lotto:
#         print(' '.join(map(str, s)))

#     # s안에 
#     for i in range(start, 7):
#         if i not in s:
#             s.append(i)
#             dfs(i+1)
#             s.pop()
# while True:
#     lotto = list(map(int, input().split()))
#     if lotto.pop(0) == 0:
#         break
#     else:
#         s = []
#         dfs(1)