'''
업 [0, 1]
다운 [0, -1]
왼쪽 [-1, 0]
오른쪽 [1, 0]
항상 0에서 시작
'''

def solution(keyinput, board):
  answer = [0, 0]
  maxPoint = [int(board[0]/2), int(board[1]/2)]
  minPoint = [-int(board[0]/2), -int(board[1]/2)]

  for i in keyinput:
    if i == "right":
      answer[0] += 1
      if answer[0] > maxPoint[0]:
        answer[0] = maxPoint[0]
    elif i == "left":
      answer[0] -= 1
      if answer[0] < minPoint[0]:
        answer[0] = minPoint[0]
    elif i == "up":
      answer[1] += 1
      if answer[1] > maxPoint[1]:
        answer[1] = maxPoint[1]
    elif i == "down":
      answer[1] -= 1
      if answer[1] < minPoint[1]:
        answer[1] = minPoint[1]

  return answer


print(solution(["left", "right", "up", "right", "right"], [11, 11]))
print(solution(["down", "down", "down", "down", "down"], [7, 9]))