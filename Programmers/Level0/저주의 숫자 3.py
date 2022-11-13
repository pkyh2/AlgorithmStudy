def solution(n):
  town_3x = []
  for i in range(1, 1000):
    if i % 3 == 0 or '3' in list(str(i)):
      continue
    else:
      town_3x.append(i)
  return town_3x[n-1]

print(solution(1))
print(solution(15))
print(solution(40))