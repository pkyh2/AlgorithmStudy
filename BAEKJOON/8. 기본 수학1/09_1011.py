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
'''
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
'''            
#어느정도 걸이가 멀어지면 어디까지 몇을 더해야 할지 모르겠음..

# 풀이 2
# 1. 거리에 따른 횟수를 계산하였더니 규칙적인 부분을 찾을 수 있었다.
# 2. 거리가 자연수의 제곱수일때는 3, 5, 7, 9...의 횟수를 가지고
# 3. 거리가 i*i-1의 곱일때는 4, 6, 8, 10...의 횟수를 가진다.
# 4. y - x의 값을 위 두개의 조건에 만족하는 수를 찾아 결과를 출력한다.

T = int(input())

def moveCounter(argument):
        result = 0
        # 거리가 1, 2, 3일때는 따로 처리
        if argument == 1:
            return 1
        elif argument == 2:
            return 2
        elif argument == 3:
            return 3

        # 4이상의 거리일때 처리
        else:
            i = 2                           # 2, 3, 4,  5,  6, 
                                            # arg = 26
            while True:
                squareNumber = i*i          # 4, 9, 16, 25, 36, 49
                squenceNumMult_plus = i * (i+1)    # 6, 12, 20, 30, 42
                squenceNumMult_minus = i * (i-1)
                if argument <= squareNumber and argument > squenceNumMult_minus:             # i*i <= 4, 9, 16, 25 / i*(i-1) > 6 12 20
                                                # arg = 26 i == 6
                    result = i + (i-1)
                    return result
                elif argument > squareNumber and argument <= squenceNumMult_plus:        # 20 25
                    result += 2 * i
                    return result
                i += 1

for i in range(T):
    
    x, y = map(int, input().split())
    distance = y - x
    print(moveCounter(distance))