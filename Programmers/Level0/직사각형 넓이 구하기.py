def solution(dots):
  answer = 0

  w1 = abs(dots[0][0] - dots[1][0])
  w2 = abs(dots[0][0] - dots[2][0])
  w3 = abs(dots[0][0] - dots[3][0])

  h1 = abs(dots[0][1] - dots[1][1])
  h2 = abs(dots[0][1] - dots[2][1])
  h3 = abs(dots[0][1] - dots[3][1])

  width = [w1, w2, w3]
  height = [h1, h2, h3]
  width.remove(0)
  height.remove(0)
  answer = width[0] * height[0]
  
  return answer

print(solution([[1, 1], [2, 1], [2, 2], [1, 2]]))
print(solution([[-1, -1], [1, 1], [1, -1], [-1, 1]]))