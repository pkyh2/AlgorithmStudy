A, B, C = map(int, input().split())

production = A + B
sale = C
cnt = 1
while True:
    if B > C:
        print(-1)
        break
    if production >= sale:
        sale += C
        production += B
        cnt += 1
    else:
        print(cnt)
        break