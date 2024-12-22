# 손익분기점

'''
고정비용 A, 한 대 생산가격 B
한 대 판매가격 C 일때,
몇 대의 노트북을 팔아야 손익이 발생하는가?
판매개수 N
A + B*N < C*N
'''
# 풀이 1(반복문)
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
# 풀이 2(방정식)
A, B, C = map(int, input().split())

if B >= C:
    print(-1)
else:
    N = A / (C - B)
    N = N + 1
    print(int(N))