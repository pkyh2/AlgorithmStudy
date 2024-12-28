T = int(input())

alphabet = "abcdefghijklmnopqrstuvwxyz"

for t in range(T):
  abc = input()
  cnt = 0
  for i, j in zip(abc, alphabet[:len(abc)]):
    if i == j:
      cnt += 1
    else:
      break

  print('#{} {}'.format(t+1, cnt))