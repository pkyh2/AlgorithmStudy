'''
정수 X의 각 자리가 등차수열을 이룬다.
ex) 123 248 321
- 1 ~ 9는 길이가 1인 등차수열
- 10 ~ 99까지는 두 수 밖에없기 때문에 공차가 몇이든 등차수열이다.
'''
# T = int(input())

# for i in range(T):
N = int(input())        # 1000보다 작은 자연수
list1 = []
for i in range(1, N+1):
    if i < 100:
        list1.append(i) # 1 ~ 99
    elif i <= 1000:
        digit_1 = (i % 10)
        digit_10 = (i // 10) % 10
        digit_100 = (i // 100)
        if digit_100 == digit_10 == digit_1:    # 111 ~ 999
            list1.append(i)
        elif digit_100 - digit_10 == digit_10 - digit_1:    # 123 ~ 789, 987 ~ 321
            list1.append(i)

print(len(list1))