'''
d(75) = 75 + 7 + 5 = 87 -> 75는 87의 생성자
- 역으로 생성자를 구하는 방법(87-> 75)을 알아야 한다. -> 불가능

- 100보다 작은 생성자를 가질 수 있는 수를 모두 구한다음
- 1 ~ 100까지 있는 list에서 제외해준다.
- 생성자를 가지는 수 구하기 100보다 작은수 일때 구하는식 n + (n // 10) + (n % 10)
- 10000보다 작은수 일때 구하는 식 i + (i // 1000) + ((i // 100) % 10) + ((i // 10)) % 10 + (i % 10)
- 중요!!! 생성자가 2개 이상인 수가 있기 때문에 한 번 제거 된 숫자는 다시 제거 할 수 없으므로
  처음 생성자보다 더 큰 수의 생성자가 나왔을때는 continue로 넘어간다.
'''

# def selfNumber(num):
#     list1 = list(range(1, 100))
#     NotSelfNum = 0
#     for i in range(1, num):
#         NotSelfNum = i + (i // 10) + (i % 10)
#         if NotSelfNum < 100:
#             list1.remove(NotSelfNum)
#     return list1

# print(selfNumber(100))

def selfNumber(num):
    list1 = list(range(1, num))
    NotSelfNum = 0
    for i in range(1, num):
        NotSelfNum = i + (i // 1000) + ((i // 100) % 10) + ((i // 10)) % 10 + (i % 10)
        if NotSelfNum <= num:
            if NotSelfNum not in list1:
                continue
            else:
                list1.remove(NotSelfNum)
    for i in list1:
        print(i)

selfNumber(10000)



# 신아님 풀이
import time
start = time.time()


def d(n):
    ans = n
    m = n
    while m > 0:
        ans += m % 10
        m = int(m / 10)
    return ans


def is_self_num(n):
    result = 1          # 결과가 1이면 출력
    digits = 0          # 자리수?
    m = n               # n은 1 ~ 10000까지 숫자를 m에 대입
    while m > 0:        # m이 양수면
        digits += 1     # 자리수 1증가 
        m = int(m / 10) # m이 0이상일 때까지 반복
    i = n - 9 * digits  # i는 
    while i < n:
        if d(i) == n:
            result = 0
            break
        i += 1
    return result


num = 1
while num <= 10000:         # 1부터 10000까지 반복
    if is_self_num(num):    # 셀프넘버면 출력
        print(num)
    num += 1                    


print("time :", time.time() - start)