def solution(chicken):
    answer = 0
    coupon = chicken
    while coupon >= 10:
      answer += coupon // 10
      coupon = coupon // 10 + coupon % 10
    return answer


'''
10장 -> 1마리
서비스 치킨에도 쿠폰 1장
'''

print(solution(100))
print(solution(1999))
print(solution(1081))