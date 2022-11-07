T = int(input())

for t in range(T):
  N = int(input())
 
  # 최댓값
  list1 = list(map(int, str(N)))
  list1_copy = list(map(int, str(N)))
  idx = 0
  # 맨앞의 숫자가 최댓값이면 중지
  if list1_copy[0] != max(list1):
    while list1_copy[0] == max(list1):
      del list1_copy[0]
      idx += 1

  # idx는 최댓값 index
  if idx == len(list1)-1:
    max = N
  else:
    list1[list1.index(max(list1[idx:]))], list1[idx] = list1[idx], list1[list1.index(max(list1[idx:]))]
    max = int("".join(map(str, list1)))
  

  # 최솟값
  list2 = list(map(int, str(N)))
  list2_copy = list(map(int, str(N)))
  idx = 0
  # 맨앞의 숫자가 최솟값이면 중지
  if list2_copy[0] != min(list1):
    while list2_copy[0] == min(list2):
      list2_copy.pop(0)
      idx += 1

  # idx는
  if idx == len(list1)-1:
    min = N
  else:
    list1[list1.index(min(list1[idx:]))], list1[idx] = list1[idx], list1[list1.index(min(list1[idx:]))]
    min = int("".join(map(str, list1)))
  

  print('#{} {} {}'.format(t+1, min, max))
