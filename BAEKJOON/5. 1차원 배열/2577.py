result = 1
for i in range(3):
    num = int(input())
    result *= num

list1 = list(map(int, str(result)))
cnt = 0
for i in range(10):
    for j in list1:

        if i == j:
            cnt += 1
    print(cnt)
    cnt = 0
