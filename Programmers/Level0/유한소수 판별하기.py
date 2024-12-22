def solution(a, b):
  answer = 1
  if a > b:
    for i in range(1, b+1):
      if a % i == 0 and b % i == 0:
        a //= i
        b //= i

    small_num = []
    idx = 2
    while idx <= b:
      if b % idx == 0:
        small_num.append(idx)
        b /= idx
      else:
        idx += 1

    for i in small_num:
      if i in [2, 5]:
        answer = 1
      else: 
        answer = 2
        break

  else:
    for i in range(1, a+1):
      if a % i == 0 and b % i == 0:
        a //= i
        b //= i

    small_num = []   
    idx = 2
    while idx <= b:
      if b % idx == 0:
        small_num.append(idx)
        b /= idx
      else:
        idx += 1

    for i in small_num:
      if i in [2, 5]:
        answer = 1
      else: 
        answer = 2
        break
  return answer


print(solution(7, 20))
print(solution(11, 22))
print(solution(12, 21))
print(solution(21, 12))
print(solution(20, 2))
print(solution(20, 1))
print(solution(4, 8))
print(solution(1, 1))
print(solution(999, 1000))
print(solution(999, 300))
