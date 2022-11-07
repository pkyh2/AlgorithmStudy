T = int(input())
days = {"SUN":0, "MON":1, "TUE":2, "WED":3, "THU":4, "FRI":5, "SAT":6}

for t in range(T):
  S = input()
  result = 7 - days[S]
  print("#{} {}".format(t+1, result))