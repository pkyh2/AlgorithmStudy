T = int(input())

for t in range(T):
  N = int(input())
  
  if N % 2 == 0:
    print('#{} {}'.format(t+1, "Alice"))
  else:
    print('#{} {}'.format(t+1, "Bob"))
