# 소수 찾기

'''
주어진 수 N개 중에서 소수가 몇 개인지 찾는 문제
소수 : 1과 자기 자신으로만 나눠지는 수
'''

# 풀이 1
# 1. 몇개의 수를 입력할지 N을 입력받는다
# 2. N번 수를 입력하고 리스트에 저장한다.
# 3. cnt변수를 만들어 소수면 cnt를 증가한다.
'''
N = int(input())
list1 = list(map(int, input().split()))

if 1 in list1:
    list1.remove(1)

for i in list1[:]:                  # 새로운 리스트에서 제거를 해줘야 한다.!!!(슬라이스로 새 리스트)
    for j in range(2, i):
        if i % j == 0:
            if i in list1:
                list1.remove(i)     # 왜 오류가 나는지 도저히 모르겠다.. -> ^ 위에서 해결

print(len(list1))
print(list1)
'''
# 풀이 2
# 1. N 입력받고, 반복문으로 N까지 반복하고 한 숫자씩 검토한다.
# 2. cnt를 만들어 소수면 횟수를 올려준다.
'''
N = int(input())

cnt2 = 0
num = list(map(int, input().split()))

if 1 in num:        # list에 1이 있으면 제거
    num.remove(1)

for i in num:
    cnt = 0
    for j in range(2, len(num)):    # i:6, 2 3 4 5
        if i % j != 0:
            cnt += 1
    if cnt > 0:
        cnt2 += 1

print(cnt2)
'''
# 풀이 3
# 1. 다 똑같은데, 나눠지면 cnt올려서 그게 양수가 아니면 소수 += 1

N = int(input())
numbers = map(int, input().split())
result = 0

for num in numbers:
    cnt = 0                     # 나눠지는 수를 세기위한 변수
    if num > 1:
        for i in range(2, num):   # 2부터 자기자신 전까지
            if num % i == 0:      # 나눠지면 cnt 증가 -> 소수가 아니라는거
                cnt += 1
        if cnt == 0:            # cnt가 0이면 -> 소수라는거
            result += 1         # 소수면 result 증가
print(result)
