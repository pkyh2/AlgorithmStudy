def solution(s):
    s = list(s.split())
    stack = []

    for i in s:
      if i == 'Z' and len(stack) != 0:
        stack.pop()
      else:
        if i == 'Z':
          continue
        stack.append(int(i))

    return sum(stack)

print(solution("Z 2 Z 3"))
print(solution("Z 20 30 Z"))
print(solution("Z Z 20 Z 1"))
print(solution("1 2 3 Z Z"))