# 설탕 배달

'''
설탕 배달 Nkg
설탕 봉지 3, 5kg
최대한 적은 봉지로 배달 ex) N == 18kg, 3kg 6봉지 보다 5kg 3봉지 3kg 1봉지 총 4봉지를 더 선호
Nkg을 정확히 만들 수 없으면 -1 출력
'''

# 풀이 1
# 1. N이 5로 나눴을때 나머지가 0이거나 3일때를 확인
# 2. 그렇지 않으면 3으로 나눴을때 나머지가 0이던지, 5이어야 한다.
# 3. N이 0보다 클때까지 반복하면서 cnt를 세어준다.
'''
N = int(input())

cnt = 0
while N > 0:
    if N % 5 == 0 or N % 5 == 3:
        if N == 3:
            N -= 3
            cnt += 1
        N -= 5
        cnt += 1
    elif N
'''
# 11같은 숫자를 해결할 수 없음

# 풀이 2
# 1. N이 12보다 클때까지 계속 5를 빼주고 cnt를 더해준다.
# 2. N이 12보다 작을때 3부터 12까지 봉지를 구할 수 있는 숫자만 cnt를 더해주고 나머지는 -1출력
# 3. 아무리 큰 수가 나와도 5키로 봉지로 다 채우고나서 나머지는 저 경우의 수밖에 없기 때문에 정답을 만족한다.

N = int(input())
cnt = 0
while N > 12:
    N -= 5
    cnt += 1

if N == 3 or N == 5:
    cnt += 1
    print(cnt)
elif N == 6 or N == 8 or N == 10:
    cnt += 2
    print(cnt)
elif N == 9 or N == 11:
    cnt += 3
    print(cnt)
elif N == 12:
    cnt += 4
    print(cnt)
else:
    print(-1)