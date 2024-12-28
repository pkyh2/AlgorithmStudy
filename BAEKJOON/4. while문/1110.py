N = int(input())
cnt = 1
new_num = N

while True:
    if N >= 10:
        temp = (new_num // 10) + (new_num % 10)
        a = (new_num % 10)
        new_num = int(str(a) + str(temp % 10))
        if new_num == N:
            print(cnt)
            break
        cnt += 1
    elif N < 10:
        temp = (new_num // 10) + (new_num % 10)
        a = (new_num % 10)
        new_num = int(str(a) + str(temp % 10))
        if new_num == N:
            print(cnt)
            break
        cnt += 1