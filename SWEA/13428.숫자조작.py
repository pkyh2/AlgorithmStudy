T = int(input())

for t in range(T):
  N = int(input())

  # 최댓값
  max_list = list(map(int, str(N)))
  max_list_copy = max_list[:]

  idx = 0
  for i in max_list:
    if i == max(max_list):
      break
    else:
      idx += 1
  
  if idx == len(max_list)-1:
    max = N
  else:
    max_index = max_list.index(max(max_list[idx:]))
    max_list[max_index], max_list[idx] = max_index[idx], max_list[max_index]
    max = int("".join(map(str, max_list)))

  print('#{} {}'.format(t+1, max))


'''
1. 최댓값
  - 각 자리 수 중에서 가장 큰 값을 맨 앞으로 보낸다.
  - 맨 앞이 가장 큰 숫자면 그 다음으로 큰 숫자를 2번째 자리로 보낸다.
  - 값을 자리를 변경할 일이 없다면 그 숫자가 최댓값이다.

2. 최솟값
  - 마찬가지

3. 값이 0일때 고려
'''