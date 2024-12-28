def solution(numlist, n):
    answer = []
    if n in numlist:
      answer.append(n)
      numlist.remove(n)
    u, d = n+1, n-1
    while len(numlist) > 0:
      if u in numlist:
        answer.append(u)
        numlist.remove(u)
      elif d in numlist:
        answer.append(d)
        numlist.remove(d)
      else:
        u +=1
        d -=1
    return answer

print(solution([1,2,3,4,5,6], 4))
print(solution([10000,20,36,47,40,6,10,7000], 30))