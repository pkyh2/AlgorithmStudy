sum = 0
for i in range(5):
    num = int(input())
    if num < 40:
        sum += 40
    else:
        sum += num

average = (sum // 5)
print(average)