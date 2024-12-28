# 덩치

'''
(몸무게, 키) (x, y)
(x, y), (p, q)에서 x > p, y > q면 (x, y)가 덩치가 더 크다
                    x > p, y < q면 같은 등수
학생 수를 입력받고 덩치를 비교해 등수를 출력하시오.
'''

# 풀이1
# 튜플로 x, y를 저장해서 리스트에 저장
# 리스트를 반복하면서 튜플을 비교한다. 
import sys
N = int(sys.stdin.readline())


muscle = []
rank = []
for _ in range(N):
    muscle.append(list(map(int, sys.stdin.readline().split())))

for i in range(len(muscle)):
    cnt = 0
    for j in range(len(muscle)):
        if muscle[i][0] < muscle[j][0] and muscle[i][1] < muscle[j][1]:     # [55, 185] [58, 183]
            cnt += 1
    rank.append(cnt + 1)

for i in rank:
    print(i, end=' ')

# 29200KB 68ms