def solution(A, B):
  answer = 0
  A_list = list(A)
  for _ in range(len(A_list)):
    if A == B:
      return answer

    A_list.insert(0, A_list.pop())
    A = ''.join(map(str, A_list))
    answer += 1


  answer = -1
  return answer


print(solution("hello", "lohel"))
print(solution("apple", "elppa"))