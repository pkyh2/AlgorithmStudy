from itertools import permutations

T = int(input())

for t in range(T):
  N = int(input())
  flag = 1

  # 입력받은 숫자의 모든 배열을 구하는 함수 호출
  number = list(map(int, str(N)))
  numbers_seperated = list(permutations(number, len(number)))
  numbers = []

  for i in numbers_seperated:
    numbers.append(int("".join(map(str, i))))

  # 입력받은 숫자의 배수가 숫자 배열안에 있으면 중지, 없으면서 숫자배열 최대값을 넘으면 중지
  i = 2
  while i*N <= max(numbers):
    if i*N in numbers:
      print('#{} {}'.format(t+1, "possible"))
      flag = 0
      break
    else:
      i += 1
  
  if flag == 1:
    print('#{} {}'.format(t+1, "impossible"))


# int형 변수를 리스트의 원소로 변환 하는 방법(feat. map)
# number = 1035
# list(map(int, str(number)))