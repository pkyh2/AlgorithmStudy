# 입력값 중에서 max값을 구하고 각 점수 / max점수 * 100을 하고 전부 더해준다.

N = int(input())
list1 = list(map(int, input().split()))
newScoreSum = 0

for i in range(N):
    maxScore = max(list1)
    newScoreSum += (list1[i] / maxScore) * 100

newAverage = newScoreSum / len(list1)
print('{:.2f}'.format(float(newAverage)))