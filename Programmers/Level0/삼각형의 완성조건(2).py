def solution(sides):
    answer = []
    _min = max(sides) - min(sides) + 1
    _max = max(sides) + min(sides)

    for i in range(_min, _max):
      answer.append(i)

    return len(answer)

print(solution([1, 2]))
print(solution([3, 6]))
print(solution([11, 7]))