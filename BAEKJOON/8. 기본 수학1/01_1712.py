# 손익분기점

# 자꾸 시간초과 발생
'''
A, B, C = map(int, input().split())

production = A + B
sale = C
cnt = 1

if B >= C:
    print(-1)
else:
    while production >= sale:
        sale += C
        production += B
        cnt += 1
    print(cnt)
'''

# 수식을 작성해서 해결
A, B, C = map(int, input().split())
 
if B >= C:
    print(-1)
else:
    N = A / (C - B)
    N = N + 1
    print(int(N))