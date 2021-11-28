# 골드바흐의 추측

'''
2보다 큰 모든 짝수는 두 소수의 합을 표현하는게 골드바흐의 파티션 ex) 4 = 2 + 2, 12 = 5 + 7
파티션이 여러가지 인 경우는 두 소수의 차이가 가장 작은 것을 출력
'''

# 풀이1 (제곱근)
# 입력한 수의 절반에 가까운 작은 소수와 그 다음소수의 합
# ex) 30 15와 가까운 작은 소수 = 13, 그 다음 소수 17
# ex) 100 절반 50, 작은 소수 = 47 그 다음 소수 53
# 예외! 4 6 10 14 같은 동일한 소수의 덧셈
T = int(input())

for _ in range(T):
    n = int(input())

    half_n = n//2

    def primeNumChecker(num):
        sieve = [True] * num
        m = int(num**0.5)

        for i in range(2, m + 1):
            if sieve[i] == True:
                for j in range(i+i, num, i):
                    sieve[j] = False

        return [i for i in range(2, num) if sieve[i] == True]

    ans1 = max(primeNumChecker(half_n+1))
    ans2 = n - ans1             # 88 43 

    print(ans1, ans2, sep=' ')

