def solution(left, right):
    answer = 0
    list1 = list(range(left, right+1))
    numbers = []
    for i in list1:
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
        if cnt % 2 == 0:
            numbers.append(i)
        else:
            numbers.append(-i)

    answer = sum(numbers)
    return answer

left = 13
right = 17
print(solution(left, right))