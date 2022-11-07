def solution(a, b):
  answer = 0

  if a > b:
    for i in range(1, b+1):
      if a % i == 0 and b % i == 0:
        a1 //= i
        b1 //= i


  return answer


print(solution(7, 20))
print(solution(11, 22))
print(solution(12, 21))
