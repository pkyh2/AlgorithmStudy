# 직각 삼각형

'''
주어진 세변의 길이로 직각삼각형인지 판단하시오.
'''

# 풀이1
# 3변을 입력받아서 제일 큰수를 판단
# 제일 큰수의 제곱이 나머지 두 수들의 제곱의 합과 같으면 "right"

while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    else:
        if a > b and a > c:             # a가 제일 긴 변
            if a*a == (b*b) + (c*c):
                print('right')
            else:
                print('wrong')
        elif b > a and b > c:           # b가 제일 긴 변
            if b*b == (a*a) + (c*c):
                print('right')
            else:
                print('wrong')
        elif c > a and c > b:           # c가 제일 긴 변
            if c*c == (a*a) + (b*b):
                print('right')
            else:
                print('wrong')

# 29200KB 72ms