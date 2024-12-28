T = int(input())

for i in range(T):
  D, L, N = map(int, input().split())
  n = 0
  Damage = D * (1 + n * (1+L*0.01))
  for j in range(L+1):
    Damage += (1 + j * (1+L*0.01))
  print('#{} {}'.format(i+1, Damage))