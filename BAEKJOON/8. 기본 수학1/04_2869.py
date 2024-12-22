# 달팽이는 올라가고 싶다

'''
A : 낮에 올라갈 수 있는 높이
B : 밤에 떨어지는 높이
V : 전체 높이
V(정상) 이상이면 밤에 미끄러지지 않는다.
'''

# 풀이 1(반복문)
#  += A - B의 반복
# 반복문 안될거같긴한데
'''
A, B, V = map(int, input().split())

height = 0
cnt = 1
while height < V:
    if height + A >= V:
        print(cnt)
        break
    else:
        height += (A - B)
        cnt += 1
'''
# 역시 안됨 => 시간초과

# 풀이 2(수식)
import math
A, B, V = map(int, input().split())

# day = V / (A - B) 는 정상에 도착했을때 밤에 미끄러지는 것을 고려하지 않았다.
day = (V - B) / (A - B)
print(math.ceil(day))