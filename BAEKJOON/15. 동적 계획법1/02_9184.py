# 신나는 함수 실행

'''
if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
    1

if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
    w(20, 20, 20)

if a < b and b < c, then w(a, b, c) returns:
    w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

otherwise it returns:
    w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
'''

import sys
input = sys.stdin.readline
# 해당 좌표의 값을 저장해야한다. -> 3차원
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if dp[a][b][c]:         # cache
        return dp[a][b][c]
    # if a < b and b < c:
    #     dp[a][b][c] =  w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    
    dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return dp[a][b][c]
# 범위가 0 ~ 20까지므로
dp = [[[0]*21 for _ in range(21)] for _ in range(21)]


while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    else:
        print('w({}, {}, {}) = {}'.format(a, b, c, w(a, b, c)))
# 30864 104


# dict를 활용한 풀이
cache = {}

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    key = '{} {} {}'.format(a, b, c)

    # 키값을 cache에 저장했다가 key값이 cache에 있으면 출력
    if key in cache:
        return cache[key]
    res = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

    cache[key] = res    # '1, 0, 1' 같은 키값에 value값 담기

    return res          # return res값들을 계산 

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    else:
        print('w({}, {}, {}) = {}'.format(a, b, c, w(a, b, c)))
# 31152 108