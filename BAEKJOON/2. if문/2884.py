H, M = map(int, input().split())
# 입력한 시간의 45분 전 시간 출력하기
# M값이 45보다 작으면 H - 1하고 M은 60 + M - 45

if H == 0:
    if M < 45:
        print('{} {}'.format(23, M + 60 - 45))
    elif M >= 45:
        print('{} {}'.format(H, M - 45))
elif H > 0:
    if M < 45:
        print('{} {}'.format(H - 1, M + 60 - 45))
    elif M >= 45:
        print('{} {}'.format(H, M - 45))