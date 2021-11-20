# Fly me to the Alpha Centauri
'''
이전 작동시기에 K광년을 이동하였을 때는 k-1, k 혹은 k+1광년만을 이동할 수 있다.
ex) 0광년을 이동하면 -1, 0, 1광년 이동할 수 있는데 -1, 0은 의미가 없으므로 1광년 이동할 수 있다.
    1광년을 이동하면 0, 1, 2광년을 이동할 수 있다. (총 1광년이동)
    다음으로 2광년을 이동하면 그 다음에는 1, 2, 3광년 중 한 거리를 이동할 수 있다. (총 1+2광년이동)
도착 지점(y)의 바로 직전(y-1) 이동거리는 반드시 1광년이어야 한다.(그러면 그 이전 이동거리는 0, 1, 2광년중 하나)

예제1
0 3
-1, 0, 1 -> 1
0, 1, 2 -> 1 도착 지점 바로 전 위치
0, 1, 2 -> 1
0 -> 1 -> 2 -> 3 
예제3
45 50
45 -> 46 -> 48 -> 49 -> 50
'''

# 풀이 1
# 1. T입력, x, y입력
# 2. spaceship = x, cnt = 0, k = 1 선언
# 3. 변수에 처음에는 무조건 1을 더하고 cnt += 1, 다다음 숫자가 y이면 

x, y = map(int, input().split())
spaceship = x
k = 1
cnt = 0

spaceship += k          # 처음 이동거리는 무조건 1이다.
cnt += 1
while spaceship <= y:   # spaceship가 증가하는데 y랑 같을 때까지만
    if k == 1:
        if spaceship + k == y:      # spaceship가 y바로 직전일때
            spaceship += k
            cnt += 1
        else:
            k += 1      # k == 2
            if spaceship + k == y:
                k -= 1
            spaceship += k
            cnt += 1
    elif 
